<template>
  <div class="readme-content">
    <h1>How to use Vertical Domain Data Anonymization</h1>

    <h2>1. 本工具可接受的待处理原文档格式</h2>
    <p>包括纯文本文件（.txt)、文字文档（.word）和pdf文档，其中word和pdf文档尽量不包含表格表单等内容，纯文字较好</p>
    <div class="image-row">
      <img class="readme-image" src="/assets/1.png" alt="示例图片1" />
      <img class="readme-image" src="/assets/2.png" alt="示例图片2" />
      <img class="readme-image" src="/assets/3.png" alt="示例图片3" />
    </div>

    <h2>2. 确认所需脱敏关键词类别</h2>

    <h3>2.1 工具自带常用脱敏关键词可勾选</h3>
    <img class="readme-image single" src="/assets/4.png" alt="工具自带关键词截图" />

    <h3>2.2 特定领域脱敏关键词按给定格式在示例中输入，工具会自动识别</h3>
    <img class="readme-image single" src="/assets/5.png" alt="特定领域关键词截图" />

    <el-alert type="warning" show-icon :closable="false" title="🌟🌟 注意用户自定义关键词的识别格式" class="my-alert" />

    <el-card class="code-block">
      <pre>
格式示例：
  张三2024年9月21日在梅花西路128号与李四签订两百块的合作协议[金额'两百块']
      </pre>
    </el-card>

    <img class="readme-image single" src="/assets/6.png" alt="关键词格式示例图" />

    <p>
      上例中的 <code>“人物”</code>、<code>“时间”</code>、<code>“地点”</code> 均在常用关键词中给出，
      用户自定义 <code>“金额”</code> 关键词需使用 
      <code>[关键词‘在文本中出现的关键词’]</code> 格式给出。
    </p>

    <h2>3. 脱敏算法选择</h2>
    <p>根据实际需求进行脱敏算法的选择</p>
    <img class="readme-image single" src="/assets/7.png" alt="算法选择界面" />

    <h3>选择效果</h3>
    <div class="image-row">
      <img class="readme-image" src="/assets/8.png" alt="选择效果示例1" />
      <img class="readme-image" src="/assets/9.png" alt="选择效果示例2" />
    </div>

    <h2>4. 选择文本输入方式</h2>
    <p>可选方式有两类，一是用户从输入框中输入，二是用户可以自行从本地中选择文件上传</p>
    <div class="image-row">
      <img class="readme-image" src="/assets/10.png" alt="文本输入框示例" />
      <img class="readme-image" src="/assets/11.png" alt="文件上传示例" />
    </div>

    <h2>5. 脱敏结果获取</h2>
    <p>脱敏后文本会返回到输出框中</p>
    <img class="readme-image single" src="/assets/12.png" alt="脱敏结果输出框" />

    <p>点击“导出结果”按钮可以下载脱敏后文档的纯文本形式</p>
    <img class="readme-image single" src="/assets/13.png" alt="导出结果按钮" />

    <p>右侧实体替换结果表可直观看出后台进行了哪些处理</p>
    <img class="readme-image single" src="/assets/14.png" alt="实体替换结果表" />
  </div>
</template>

<script>
export default {
  name: 'ReadmeGuideExtended'
}
</script>

<style scoped>
.readme-content {
  font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  background-color: #f8f9fa;
  color: #333;
  padding: 40px;
  line-height: 2;
  font-size: 16px;
}

h1 {
  color: #2c3e50;
  font-size: 30px;
  border-bottom: 2px solid #ccc;
  padding-bottom: 8px;
}

h2 {
  color: #34495e;
  font-size: 24px;
  margin-top: 32px;
  border-left: 4px solid #409EFF;
  padding-left: 12px;
}

h3 {
  color: #3b5998;
  font-size: 20px;
  margin-top: 24px;
}

.code-block {
  background-color: #f4f4f4;
  padding: 16px;
  margin: 16px 0;
  font-family: 'Courier New', monospace;
  font-size: 14px;
  box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.05);
  white-space: pre-wrap;
}

code {
  background-color: #f0f0f0;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  color: #3d527d;
}

.readme-image {
  width: 35%;
  margin: 16px 0;
  display: block;
  border-radius: 8px;
  border: 1px solid #ddd;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.readme-image.single {
  max-width: 60%;
}

.image-row {
  display: flex;
  justify-content: flex-start;
  gap: 12px;
  margin: 16px 0;
}

.image-row img.readme-image {
  max-width: 32%;
  margin: 0;
}

.my-alert {
  margin: 20px 0;
}
</style>