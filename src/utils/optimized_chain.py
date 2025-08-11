# DataMasker-backend-twice/utils/optimized_chain.py
import os
import re
import time
from datetime import datetime
import config
from utils import tools, readDoc
from utils.splitDoc import split

# 全局缓存，避免重复计算
word_cache = {}
sentence_cache = {}

def optimized_final(path, entity_type, demos, patten=2):
    """优化版本的处理链，减少API调用"""
    print("🚀 启动优化版数据脱敏处理...")
    
    # 清理缓存
    global word_cache, sentence_cache
    word_cache = {}
    sentence_cache = {}
    
    # 更新配置
    config.Config.entities = entity_type
    config.Config.demos = demos
    config.Config.docPath = path
    
    # 读取文档
    print("📖 读取文档...")
    docs = readDoc.read_doc_content(path)
    split_docs = split(docs)
    
    sensitive_words = {}
    replace_dict = {}
    
    # 批量处理每个文档片段
    for i, doc in enumerate(split_docs):
        print(f"🔄 处理片段 {i+1}/{len(split_docs)}")
        text = doc.page_content
        
        # 简单的预过滤，减少API调用
        if len(text.strip()) < 3:
            continue
            
        # 使用规则预过滤明显不包含敏感信息的文本
        if is_likely_sensitive(text, entity_type):
            # 一次性识别整个片段的敏感词
            sensitive_words_in_text = batch_identify_sensitive_words(text, entity_type, demos)
            sensitive_words.update(sensitive_words_in_text)
            
            # 添加小延迟避免API限流
            time.sleep(1)
    
    # 批量替换敏感词
    if sensitive_words:
        print(f"🔒 发现 {len(sensitive_words)} 个敏感词，开始替换...")
        replace_dict = batch_replace_words(sensitive_words, patten)
    
    # 应用替换
    for doc in split_docs:
        for original, replacement in replace_dict.items():
            doc.page_content = doc.page_content.replace(original, replacement)
    
    # 保存结果
    merged_text = "".join([doc.page_content for doc in split_docs])
    
    basename = os.path.basename(path)
    time_sample = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(config.Config.outputPath, f"{time_sample}_{basename}")
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(merged_text)
    
    print(f"✅ 处理完成，结果保存到: {file_path}")
    return file_path, replace_dict

def is_likely_sensitive(text, entity_types):
    """规则预过滤，减少不必要的API调用"""
    # 基本规则：包含中文字符、数字、特殊模式等
    patterns = {
        '人名': r'[\u4e00-\u9fa5]{2,4}(?=先生|女士|医生|教授|主任|经理|总监|先|小|老)',
        '时间': r'\d{4}年\d{1,2}月\d{1,2}日|\d{1,2}月\d{1,2}日|\d{4}-\d{1,2}-\d{1,2}',
        '地点': r'[\u4e00-\u9fa5]+(?:省|市|区|县|街道|路|号|院|楼)',
        '电话': r'1[3-9]\d{9}|\d{3,4}-\d{7,8}',
        '邮箱': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        '身份证': r'\d{15}|\d{18}|\d{17}[Xx]'
    }
    
    # 如果文本匹配任何模式，认为可能包含敏感信息
    for entity in entity_types.split('、'):
        if entity in patterns:
            if re.search(patterns[entity], text):
                return True
    
    # 简单启发式：包含数字和中文的文本更可能包含敏感信息
    has_chinese = bool(re.search(r'[\u4e00-\u9fa5]', text))
    has_number = bool(re.search(r'\d', text))
    
    return has_chinese and (has_number or len(text) > 20)

def batch_identify_sensitive_words(text, entity_type, demos):
    """批量识别敏感词，减少API调用次数"""
    # 检查缓存
    cache_key = f"{text[:50]}_{entity_type}"
    if cache_key in sentence_cache:
        return sentence_cache[cache_key]
    
    # 构造批量识别提示
    prompt = f"""
请识别以下文本中的敏感信息：

文本：{text}

需要识别的敏感信息类型：{entity_type}

示例：{demos}

请直接返回格式：敏感词1|敏感词2|敏感词3
如果没有敏感信息，返回：无
"""
    
    try:
        result = config.Config.LLM._call(prompt)
        sensitive_words = {}
        
        if result and result.strip() != "无":
            words = [w.strip() for w in result.split('|') if w.strip()]
            for word in words:
                if word in text:  # 验证词确实在文本中
                    sensitive_words[word] = text
        
        # 缓存结果
        sentence_cache[cache_key] = sensitive_words
        return sensitive_words
        
    except Exception as e:
        print(f"❌ 批量识别失败: {e}")
        return {}

def batch_replace_words(sensitive_words, patten):
    """批量替换敏感词"""
    replace_dict = {}
    
    if patten == 1:
        # 简单遮蔽模式，不需要API调用
        for word in sensitive_words.keys():
            if len(word) <= 2:
                replace_dict[word] = "*" * len(word)
            else:
                replace_dict[word] = word[0] + "*" * (len(word) - 2) + word[-1]
    
    elif patten == 2:
        # 智能替换模式，批量处理
        words_list = list(sensitive_words.keys())
        batch_size = 5  # 每批处理5个词
        
        for i in range(0, len(words_list), batch_size):
            batch = words_list[i:i + batch_size]
            batch_prompt = f"""
请为以下敏感词提供合适的替换词：

敏感词列表：{', '.join(batch)}

要求：
1. 保持语义合理性
2. 每个替换词用|分隔
3. 按原顺序返回

格式：替换词1|替换词2|替换词3
"""
            
            try:
                result = config.Config.LLM._call(batch_prompt)
                if result:
                    replacements = [r.strip() for r in result.split('|')]
                    for j, word in enumerate(batch):
                        if j < len(replacements) and replacements[j]:
                            replace_dict[word] = replacements[j]
                        else:
                            # 备用简单替换
                            replace_dict[word] = f"[{word[0] if word else '敏感信息'}***]"
                
                # 添加延迟避免API限流
                time.sleep(2)
                
            except Exception as e:
                print(f"❌ 批量替换失败: {e}")
                # 备用简单替换
                for word in batch:
                    replace_dict[word] = f"[{word[0] if word else '敏感信息'}***]"
    
    else:
        # 其他模式的处理
        for word in sensitive_words.keys():
            replace_dict[word] = f"[{word[0] if word else '敏感信息'}***]"
    
    return replace_dict