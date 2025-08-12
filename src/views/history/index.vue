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
        @click="goToDetail(record.id)"
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
            @click.stop="handleDelete(index)"
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
  name: 'HistoryList',
  data() {
    return {
      records: [
        { id: 1, type: 'pdf', name: '财务报表2023', time: '2023-05-12T14:30:00', isHovered: false },
        { id: 2, type: 'word', name: '项目计划书初稿', time: '2023-05-11T09:15:00', isHovered: false },
        { id: 3, type: 'txt', name: '会议记录0428', time: '2023-05-10T16:45:00', isHovered: false },
        { id: 4, type: 'text', name: '这是一段纯文本的测试内容用来演示', time: '2023-05-09T11:20:00', isHovered: false },
        { id: 5, type: 'pdf', name: '用户使用手册', time: '2023-05-08T13:10:00', isHovered: false },
        { id: 6, type: 'word', name: '合同范本', time: '2023-05-07T10:05:00', isHovered: false }
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
      console.log('删除记录:', index);
      // this.records.splice(index, 1);
    },
    goToDetail(id) {
      this.$router.push({ name: 'HistoryDetail', params: { id } });
    }
  }
}
</script>

<style scoped>
/* 保持之前的样式不变 */
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
  border-radius: 8px;
  overflow: hidden;
}

.history-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  transition: background-color 0.2s;
  margin-bottom: 8px;
  border-radius: 6px;
  cursor: pointer;
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
  font-size: 14px;
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
  font-size: 16px;
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
  font-size: 16px;
  margin-right: 16px;
}

.delete-btn {
  background: none;
  border: none;
  color: #999;
  font-size: 20px;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.2s, background-color 0.2s;
  width: 30px;
  height: 30px;
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