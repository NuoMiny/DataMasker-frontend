<template>
  <div class="history-container">
    <h2>历史记录</h2>
    <div class="history-list">
      <div 
        v-for="(record, index) in records" 
        :key="index" 
        class="history-item"
        @mouseover="hoverItem(index)"
        @mouseleave="leaveItem(index)"
      >
        <div class="item-left">
          <div class="file-icon">
            <span v-if="record.type === 'pdf'" class="icon-pdf">PDF</span>
            <span v-else-if="record.type === 'word'" class="icon-word">DOC</span>
            <span v-else-if="record.type === 'txt'" class="icon-txt">TXT</span>
            <span v-else class="icon-text">TEXT</span>
          </div>
          <div class="file-name">
            {{ record.type === 'text' ? record.name.substring(0, 10) + (record.name.length > 10 ? '...' : '') : record.name }}
          </div>
        </div>
        <div class="item-right">
          <div class="time">{{ formatTime(record.time) }}</div>
          <button 
            class="delete-btn" 
            :class="{ 'show-btn': record.isHovered }"
            @click="handleDelete(index)"
          >
            ×
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HistoryPage',
  data() {
    return {
      records: [
        { type: 'pdf', name: '财务报表2023', time: '2023-05-12T14:30:00', isHovered: false },
        { type: 'word', name: '项目计划书初稿', time: '2023-05-11T09:15:00', isHovered: false },
        { type: 'txt', name: '会议记录0428', time: '2023-05-10T16:45:00', isHovered: false },
        { type: 'text', name: '这是一段纯文本的测试内容用来演示', time: '2023-05-09T11:20:00', isHovered: false },
        { type: 'pdf', name: '用户使用手册', time: '2023-05-08T13:10:00', isHovered: false },
        { type: 'word', name: '合同范本', time: '2023-05-07T10:05:00', isHovered: false }
      ]
    }
  },
  methods: {
    formatTime(timeString) {
      const date = new Date(timeString);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      const hours = String(date.getHours()).padStart(2, '0');
      const minutes = String(date.getMinutes()).padStart(2, '0');
      
      return `${year}-${month}-${day} ${hours}:${minutes}`;
    },
    hoverItem(index) {
      this.records[index].isHovered = true;
    },
    leaveItem(index) {
      this.records[index].isHovered = false;
    },
    handleDelete(index) {
      // 删除记录的逻辑
      console.log('删除记录:', index);
      // this.records.splice(index, 1);
    }
  }
}
</script>

<style scoped>
.history-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h2 {
  color: #333;
  margin-bottom: 20px;
}

.history-list {
  /* 移除了边框 */
  border-radius: 8px;
  overflow: hidden;
}

.history-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  /* 移除了底部边框 */
  transition: background-color 0.2s;
  margin-bottom: 8px;
  border-radius: 6px;
}

.history-item:hover {
  background-color: #f5f5f5;
}

.item-left {
  display: flex;
  align-items: center;
  flex: 1;
}

.file-icon {
  margin-right: 12px;
}

.file-icon span {
  display: inline-block;
  width: 40px;
  height: 40px;
  line-height: 40px;
  text-align: center;
  border-radius: 6px;
  color: white;
  font-size: 12px;
  font-weight: bold;
}

.icon-pdf {
  background: linear-gradient(to bottom, #f7581e, #c93131);
}

.icon-word {
  background: linear-gradient(to bottom, #1879da, #1956b8);
}

.icon-txt {
  background: linear-gradient(to bottom, #bcbcbc, #7c7c7c);
}

.icon-text {
  background: linear-gradient(to bottom, #50c966, #2aa35e);
}

.file-name {
  color: #333;
  font-size: 14px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 400px;
}

.item-right {
  display: flex;
  align-items: center;
}

.time {
  color: #999;
  font-size: 12px;
  margin-right: 16px;
}

.delete-btn {
  background: none;
  border: none;
  color: #999;
  font-size: 18px;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.2s, background-color 0.2s;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.delete-btn:hover {
  background-color: #e0e0e0;
  color: #666;
}

.show-btn {
  opacity: 1;
}
</style>