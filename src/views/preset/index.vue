<template>
  <div class="background-wrapper">
    <div class="color-gradient-layer"></div>
    <div class="opacity-gradient-layer"></div>
    
    <div class="preset-container">
      <h1 class="page-title">脱 敏 预 设</h1>
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
          description: '适用于各类商务合同文档的脱敏处理，保护商业机密和个人隐私信息。',
          keywords: '金额,公司名称,签约方,银行账号,联系方式,日期,地址,身份证号,法人代表,产品名称,规格型号'
        },
        {
          id: 2,
          title: '法律文书',
          description: '法律文件专用脱敏模板，有效保护案件相关敏感信息。',
          keywords: '当事人,案号,身份证,住址,联系方式,判决结果,财产信息'
        },
        {
          id: 3,
          title: '学术报告',
          description: '学术研究数据脱敏方案，确保研究数据可用性的同时保护隐私。',
          keywords: '实验对象,个人信息,机构名称,地理位置,时间数据'
        },
        {
          id: 4,
          title: '医疗记录',
          description: '医疗健康数据脱敏处理，符合HIPAA等隐私保护法规要求。',
          keywords: '患者ID,姓名,年龄,诊断结果,用药信息,检查报告,医生姓名'
        },
        {
          id: 5,
          title: '金融报表',
          description: '财务报表数据脱敏，保护企业财务敏感信息。',
          keywords: '金额,账户,交易流水,客户信息,日期,分支机构'
        },
        {
          id: 6,
          title: '人事档案',
          description: '员工信息脱敏处理，保护员工隐私同时满足管理需求。',
          keywords: '姓名,身份证号,薪资,联系方式,家庭住址,教育背景,工作经历'
        },
        {
          id: 7,
          title: '电商订单',
          description: '电子商务交易数据脱敏，保护客户购物隐私和支付信息。',
          keywords: '订单号,用户名,手机号,收货地址,支付金额,银行卡号,商品详情'
        },
        {
          id: 8,
          title: '教育档案',
          description: '学生信息与成绩数据脱敏方案，符合教育隐私保护要求。',
          keywords: '学号,姓名,家庭情况,考试成绩,教师评语,联系方式,宿舍信息'
        },
        {
          id: 9,
          title: '政务公开',
          description: '政府公文脱敏处理，平衡信息公开与隐私保护需求。',
          keywords: '公民姓名,身份证号,住址,联系方式,财产信息,审批编号'
        },
        {
          id: 10,
          title: '保险单据',
          description: '保险行业专用脱敏模板，保护投保人敏感信息。',
          keywords: '保单号,投保人,受益人,健康状况,财产状况,联系方式,银行账号'
        },
        {
          id: 11,
          title: '物流运输',
          description: '物流快递信息脱敏方案，保护收发件人隐私。',
          keywords: '运单号,发件人,收件人,联系方式,详细地址,物品内容,保价金额'
        },
        {
          id: 12,
          title: '社交媒体',
          description: '社交平台用户数据脱敏，适用于数据分析场景。',
          keywords: '用户名,昵称,联系方式,地理位置,IP地址,好友关系,聊天记录'
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
        if (totalLength + kw.length > 20) {
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
      
      this.$router.push({ name: 'PresetDetail', params: { id } });
    }
  }
}
</script>

<style scoped>
/* 外层容器设置 */
.background-wrapper {
  position: relative;
  min-height: 100vh;
  width: 100%;
}

/* 颜色层 */
.color-gradient-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    135deg,
    rgb(83, 189, 159) 0%,
    rgb(120, 182, 151) 25%,
    rgb(93, 168, 104) 40%,
    rgb(149, 189, 112) 70%,
    rgb(172, 226, 78) 100%
  );
  z-index: 1;
}

/* 透明度层 */
.opacity-gradient-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 1) 0%,
    rgba(255, 255, 255, 0.3) 100%
  );
  z-index: 2;
}

/* 内容容器设置 */
.preset-container {
  position: relative;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  z-index: 3;
}

.page-title {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
  font-size: 48px;
  color: #325f32;
}

.card-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.preset-card {
  background-color: rgba(255, 255, 255, 0.9);
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