<template>
  <div class="page-backgound">
    <div class="preset-detail-container">
        <h1 class="page-title">{{ preset.title }}</h1>
        
        <!-- 预设简介卡片 -->
        <div class="description-section">
        <div class="card-title">简介</div>
        <div class="description-content">{{ preset.description }}</div>
        </div>

        <!-- 预设卡片区域 -->
        <div class="preset-section">
        <div class="section-header">
            <div class="preset-title">预设</div>
            <button class="copy-btn" @click="copyPresets">复制预设</button>
        </div>
        
        <div class="preset-content">
            <div class="preset-box">
            <div class="sub-title">关键词</div>
            <div class="tags-container">
                <span 
                v-for="(keyword, index) in preset.keywords" 
                :key="index" 
                class="preset-tag"
                >
                {{ keyword }}
                </span>
            </div>
            </div>
            
            <div class="example-box">
            <div class="sub-title">自定义输入示例</div>
            <div class="example-content">{{ exampleText }}</div>
            </div>
        </div>
        </div>

        <!-- 脱敏模式区域 -->
        <div class="desensitization-mode">
        <div class="card-title">脱敏模式</div>
        <div class="mode-tags">
            <span class="mode-tag">{{ preset.mode }}</span>
        </div>
        </div>

        <!-- 示例对比区域 -->
        <div class="example-section">
        <div class="card-title">示例</div>
        <div class="example-comparison">
            <div class="example-column">
            <div class="column-title">脱敏前</div>
            <div class="example-text before-text">{{ beforeExample }}</div>
            </div>
            <div class="example-column">
            <div class="column-title">脱敏后</div>
            <div class="example-text after-text">{{ afterExample }}</div>
            </div>
        </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PresetDetail',
  data() {
    return {
      // 模拟数据 - 实际应用中应该从API获取，根据路由参数获取对应ID的预设
      preset: {
        id: 1,
        title: '商务合同',
        keywords: ['金额', '公司名称', '签约方', '银行账号', '联系方式', '日期', '地址', '身份证号'],
        mode: '关键词模糊',
        description: '适用于各类商务合同文档的脱敏处理，保护商业机密和个人隐私信息。'
      },
      exampleText: '本合同约定甲方（某某科技有限公司）向乙方（张三）支付金额￥50,000元，乙方银行账号：622588******1234，签约日期：2023年10月15日。',
      beforeExample: '甲方：某某科技有限公司\n乙方：张三\n合同金额：￥50,000元\n乙方银行账号：6225881234561234\n联系电话：13800138000\n签约日期：2023年10月15日\n联系地址：北京市海淀区某某路1号\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1',
      afterExample: '甲方：**科技有限公司\n乙方：**\n合同金额：￥**元\n乙方银行账号：622588******1234\n联系电话：138****8000\n签约日期：****年**月**日\n联系地址：北京市**区某某路*号'
    }
  },
  methods: {
    copyPresets() {
      const data = {
        keywords: this.presets,
        example: this.exampleText
      };
      const text = JSON.stringify(data, null, 2);
      this.copyToClipboard(text);
      this.$message.success('预设已复制到剪贴板');
    }
  }
}
</script>

<style scoped>
.page-backgound{
  background-color: #ecf4f0;
}

.preset-detail-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

/* 页面标题样式 */
.page-title {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  color: #325f32;
  margin-bottom: 30px;
}

/* 简介卡片区域 */
.description-section {
  margin-bottom: 10px;
  background: #fff;
  border: 1px solid #e0e0e0;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.description-content {
  font-size: 16px;
  line-height: 1.6;
  color: #555;
  white-space: pre-wrap;
}

/* 预设卡片区域 */
.preset-section {
  margin-bottom: 10px;
  background: #fff;
  border: 1px solid #e0e0e0;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.preset-title {
  font-weight: bold;
  color: #333;
  font-size: 18px;
  margin: 0;
}

.preset-content {
  display: flex;
  gap: 20px;
}

.preset-box, .example-box {
  flex: 1;
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 15px;
}

.card-title{
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 20px;
}

.sub-title {
  font-weight: bold;
  margin-bottom: 10px;
  color: #666;
  font-size: 16px;
}

.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.preset-tag {
  background: #f0f9eb;
  color: #67c23a;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 14px;
}

.example-content {
  white-space: pre-wrap;
  font-size: 16px;
  line-height: 1.6;
  color: #555;
  padding: 8px;
  background: #f9f9f9;
  border-radius: 4px;
  min-height: 60px;
}

.copy-btn {
  background: #a6a6a6;
  border: 0px;
  color: #fff;
  border-radius: 4px;
  padding: 8px 15px;
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: all 0.2s;
  font-size: 14px;
  height: fit-content;
}

.copy-btn:hover {
  background: #b7b7b7;
}

/* 脱敏模式区域 */
.desensitization-mode {
  margin-bottom: 10px;
  background: #fff;
  border: 1px solid #e0e0e0;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.mode-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.mode-tag {
  background: #f0f9eb;
  color: #67c23a;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 14px;
}

/* 示例对比区域 */
.example-section {
  margin-bottom: 10px;
  background: #fff;
  border: 1px solid #e0e0e0;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.example-comparison {
  display: flex;
  gap: 20px;
}

.example-column {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.column-title {
  font-weight: bold;
  margin-bottom: 10px;
  color: #666;
  font-size: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid #e0e0e0;
}

.example-text {
  white-space: pre-wrap;
  font-size: 16px;
  line-height: 1.6;
  padding: 15px;
  border-radius: 4px;
  flex-grow: 1;
  height: 300px;
  overflow-y: auto;
  background-color: #fafafa;
  border: 1px solid #eee;
  color: #333;
}

.before-text {
  background-color: #fff8f8;
}

.after-text {
  background-color: #f4fff4;
}
</style>