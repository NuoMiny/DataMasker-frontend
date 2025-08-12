<template>
  <div class="detail-container">
    <!-- 预设展示区 -->
    <div class="preset-section">
      <div class="preset-title">脱敏预设</div>
      <div class="preset-box">
        <span 
          v-for="(preset, index) in presets" 
          :key="index" 
          class="preset-tag"
        >
          {{ preset }}
        </span>

      </div>
      <button class="copy-btn" @click="copyPresets">
        <span class="copy-icon">⎘</span> 复制预设
      </button>
    </div>
    
    <!-- 内容展示区 -->
    <div class="content-section">
      <div class="text-box original-box">
        <div class="box-header">
          <div class="box-title">脱敏前文本</div>
          <button class="copy-btn" @click="copyOriginalText">
            <span class="copy-icon">⎘</span> 复制
          </button>
        </div>
        <div class="box-content">{{ originalText }}</div>
      </div>
      
      <div class="text-box desensitized-box">
        <div class="box-header">
          <div class="box-title">脱敏后文本</div>
          <button class="copy-btn" @click="copyDesensitizedText">
            <span class="copy-icon">⎘</span> 复制
          </button>
        </div>
        <div class="box-content">{{ desensitizedText }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HistoryDetail',
  data() {
    return {
      // 模拟数据 - 实际应从API获取
      presets: ['金额', '时间', '工作单位', '身份证号', '手机号码', '手机号码', '手机号码', '手机号码', '手机号码', '手机号码', '手机号码', '手机号码', '手机号码', '手机号码', '手机号码', '手机号码', '手机号码'],
      originalText: `这是一段包含敏感信息的文本示例：
      用户姓名：张三
      身份证号：320***********1234
      手机号码：138****5678
      工作单位：某某科技有限公司
      交易金额：¥5,000.00
      交易时间：2023-05-15 14:30
      1
      1
      1
      1
      1
      1
      1
      1
      1
      1
      1
      1
      1
      1
      `,
      desensitizedText: `这是一段包含敏感信息的文本示例：
      用户姓名：*三
      身份证号：****************
      手机号码：********
      工作单位：某某科技****
      交易金额：¥******
      交易时间：**********`
    }
  },
  created() {
    const recordId = this.$route.params.id;
    console.log('加载历史记录ID:', recordId);
  },
  methods: {
    copyPresets() {
      const text = this.presets.join(',');
      this.copyToClipboard(text);
      this.$message.success('预设已复制到剪贴板');
    },
    
    copyOriginalText() {
      this.copyToClipboard(this.originalText);
      this.$message.success('脱敏前文本已复制到剪贴板');
    },
    
    copyDesensitizedText() {
      this.copyToClipboard(this.desensitizedText);
      this.$message.success('脱敏后文本已复制到剪贴板');
    },
    
    copyToClipboard(text) {
      const textarea = document.createElement('textarea');
      textarea.value = text;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
    }
  }
}
</script>

<style scoped>
.detail-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h2 {
  color: #333;
  margin-bottom: 20px;
}

.preset-section {
  margin-bottom: 30px;
  background: #fff;
  border: 1px solid #e0e0e0;
  padding: 20px;
  border-radius: 8px;
}


.preset-title {
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
  font-size: 18px;
}

.preset-box {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
  position: relative;
  min-height: 60px;
  padding-top: 6px;
}



.preset-tag {
  background: #f0f9eb;
  color: #67c23a;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 16px;
}

.copy-btn {
  background: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 6px 12px;
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: all 0.2s;
  margin-left: auto;
  font-size: 16px;
}

.copy-btn:hover {
  background: #f0f0f0;
}

.copy-icon {
  margin-right: 5px;
  font-size: 18px;
}

.content-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.text-box {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  transition: background-color 0.2s;
  height: 370px;
  display: flex;
  flex-direction: column;
}

.box-header {
  background: #f5f5f5;
  padding: 12px 15px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #e0e0e0;
  font-size: 18px;
}

.box-title {
  font-weight: bold;
  color: #333;
}

.box-content {
  white-space: pre-wrap;
  font-size: 16px;
  line-height: 1.6;
  color: #555;
  padding: 15px;
  flex-grow: 1;
  overflow-y: auto;
}

.original-box {
  border-top: 3px solid #a0c4ff;
}

.desensitized-box {
  border-top: 3px solid #b5ead7;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .content-section {
    grid-template-columns: 1fr;
  }
  
  .text-box {
    height: 300px;
  }
}
</style>