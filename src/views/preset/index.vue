<template>
  <div class="preset-container">
    <h1 class="page-title">脱敏预设</h1>
    <div class="card-list">
      <div 
        v-for="preset in presetList" 
        :key="preset.id"
        class="preset-card"
        @click="goToDetail(preset.id)"
        @mouseover="hoverCard(preset.id)"
        @mouseleave="leaveCard(preset.id)"
        :class="{ 'card-hover': hoverStates[preset.id] }"
      >
        <h3 class="card-title">{{ preset.title }}</h3>
        <p class="card-desc">{{ preset.description }}</p>
        <div class="card-keywords-container">
          <div class="card-keywords">
            <span v-for="(keyword, index) in formatKeywords(preset.keywords)" :key="index">
              {{ keyword }}<span v-if="index < formatKeywords(preset.keywords).length - 1">, </span>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PresetList',
  data() {
    return {
      presetList: [], // 预设列表
      hoverStates: {}, // 记录卡片悬停状态
      // 模拟数据 - 实际应用中应该从API获取
      mockData: [
        {
          id: 1,
          title: '商务合同',
          description: '适用于各类商务合同文档的脱敏处理，保护商业机密和个人隐私信息。适用于各类商务合同文档的脱敏处理，保护商业机密和个人隐私信息。适用于各类商务合同文档的脱敏处理，保护商业机密和个人隐私信息。',
          keywords: '金额,公司名称,签约方,银行账号,联系方式,日期,地址,身份证号,法人代表,产品名称,规格型号'
        },
        {
          id: 2,
          title: '法律文书',
          description: '法律文件专用脱敏模板，有效保护案件相关敏感信息。法律文件专用脱敏模板，有效保护案件相关敏感信息。法律文件专用脱敏模板，有效保护案件相关敏感信息。',
          keywords: '当事人,案号,身份证,住址,联系方式,判决结果,财产信息'
        },
        {
          id: 3,
          title: '学术报告',
          description: '学术研究数据脱敏方案，确保研究数据可用性的同时保护隐私。学术研究数据脱敏方案，确保研究数据可用性的同时保护隐私。',
          keywords: '实验对象,个人信息,机构名称,地理位置,时间数据'
        },
        {
          id: 4,
          title: '医疗记录',
          description: '医疗健康数据脱敏处理，符合HIPAA等隐私保护法规要求。医疗健康数据脱敏处理，符合HIPAA等隐私保护法规要求。',
          keywords: '患者ID,姓名,年龄,诊断结果,用药信息,检查报告,医生姓名'
        },
        {
          id: 5,
          title: '金融报表',
          description: '财务报表数据脱敏，保护企业财务敏感信息。财务报表数据脱敏，保护企业财务敏感信息。',
          keywords: '金额,账户,交易流水,客户信息,日期,分支机构'
        },
        {
          id: 6,
          title: '人事档案',
          description: '员工信息脱敏处理，保护员工隐私同时满足管理需求。员工信息脱敏处理，保护员工隐私同时满足管理需求。',
          keywords: '姓名,身份证号,薪资,联系方式,家庭住址,教育背景,工作经历'
        }
      ]
    }
  },
  created() {
    this.fetchPresetList();
  },
  methods: {
    // 模拟从后台获取预设列表
    fetchPresetList() {
      // 这里应该是API请求，现在使用模拟数据
      // axios.get('/api/presets').then(response => {
      //   this.presetList = response.data;
      // });
      
      // 使用模拟数据
      this.presetList = this.mockData;
      
      // 初始化悬停状态
      this.presetList.forEach(preset => {
        this.$set(this.hoverStates, preset.id, false);
      });
    },
    // 格式化关键词显示
    formatKeywords(keywords) {
      const keywordArray = keywords.split(',');
      let result = [];
      let totalLength = 0;
      
      for (let i = 0; i < keywordArray.length; i++) {
        const kw = keywordArray[i].trim();
        if (totalLength + kw.length > 10) {
          if (i === 0) {
            // 如果第一个关键词就超过10个字符，截断它
            result.push(kw.substring(0, 7) + '...');
          } else {
            // 否则添加省略号
            result.push('...');
          }
          break;
        }
        result.push(kw);
        totalLength += kw.length;
        if (i < keywordArray.length - 1) {
          totalLength += 2; // 逗号和空格的长度
        }
      }
      
      return result;
    },
    // 鼠标悬停卡片
    hoverCard(id) {
      this.$set(this.hoverStates, id, true);
    },
    // 鼠标离开卡片
    leaveCard(id) {
      this.$set(this.hoverStates, id, false);
    },
    // 跳转到详情页
    goToDetail(id) {
      // 实际应用中应该使用路由跳转
      // this.$router.push(`/preset/detail/${id}`);
      
      // 这里简单模拟一下
      alert(`跳转到预设详情页，ID: ${id}`);
      console.log(`跳转到预设详情页，ID: ${id}`);
    }
  }
}
</script>

<style scoped>
.preset-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.page-title {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.card-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.preset-card {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  height: 150px; /* 固定卡片高度 */
  position: relative; /* 为关键词定位做准备 */
}

.preset-card:hover {
  transform: translateY(-5px);
}

.card-hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.card-title {
  color: #325f32; /* 深绿色 */
  margin-top: 0;
  margin-bottom: 10px;
  font-size: 18px;
  font-weight: bold;
}

.card-desc {
  color: #666;
  font-size: 14px;
  line-height: 1.5;
  margin: 10px 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  height: 3em;
  flex-shrink: 0;
}

.card-keywords-container {
  position: absolute;
  bottom: 20px; /* 与卡片底部保持固定距离 */
  left: 20px;
  right: 20px;
}

.card-keywords {
  display: flex;
  flex-wrap: wrap;
  font-size: 12px;
  color: #888;
  padding-top: 10px;
  border-top: 1px solid #eee; /* 添加分割线 */
}

.card-keywords span {
  margin-right: 5px;
}
</style>