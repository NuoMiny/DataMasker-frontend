<template>
  <div class="text-box">
    <h4>输出处理后文本（txt格式）</h4>
    <el-input
      type="textarea"
      :rows="15"
      readonly
      :value="value"
      resize="none"
      class="output-area"
    />
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: ''
    }
  }
};
</script>

<style scoped>
.output-area {
  position: relative;
}

.output-area :deep(.el-textarea__inner) {
  background-color: #f8f9fa;
  cursor: default;
  font-family: Monaco, Consolas, monospace;
  line-height: 1.5;
  white-space: pre-wrap;
}
</style>