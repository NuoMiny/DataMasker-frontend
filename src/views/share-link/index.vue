<template>
    <div class="app-container">
      <el-alert
        title="网站链接已复制到剪贴板！"
        type="success"
        show-icon
        :closable="false"
      />
    </div>
  </template>
  
  <script>
  export default {
    mounted() {
      const url = window.location.origin
      navigator.clipboard.writeText(url).then(() => {
        console.log('链接已复制：', url)
      }).catch(() => {
        this.$message.error('复制失败，请手动复制链接')
      })
    }
  }
  </script>