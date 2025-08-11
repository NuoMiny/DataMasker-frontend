<template>
  <div>
    <!-- 外层根元素 START -->
    <div class="container">
      <el-row :gutter="20">
        <!-- 左侧控制面板 -->
        <el-col :span="10">
          <el-card class="box-card">
            <div slot="header">
           <span style="font-size: 20px; font-weight: bold;">控制面板</span>
           </div>


            <!-- 特殊示例输入 -->
            <div class="control-section">
              <h4>特殊示例输入</h4>
              <el-input
                type="textarea"
                :rows="3"
                v-model="exampleText"
                placeholder="示例：[姓名'张三'][时间'2024年9月21日']..."
              ></el-input>
              <div class="flex-between mt-10">
                <!-- 深绿色“提取”按钮，悬停变浅，按下变深 -->
                <el-button
                  size="small"
                  @click="parseExample"
                  :disabled="!exampleText"
                  @mouseenter="hoverExtract = true"
                  @mouseleave="hoverExtract = false"
                  @mousedown.native="pressedExtract = true"
                  @mouseup.native="pressedExtract = false"
                  :style="{
                    backgroundColor: pressedExtract ? '  #98b0a3' : (hoverExtract ? '#3e7b5a' : '#2e5c42'),
                    borderColor: pressedExtract ? '#ecf4f0' : (hoverExtract ? '#3e7b5a' : '#2e5c42'),
                    color: '#fff',
                    transition: 'all 0.2s ease',
                    transform: pressedExtract ? 'scale(0.98)' : 'scale(1)'
                  }"
                >提取</el-button>

                <!-- 红色“清空”按钮保持默认 danger 类型 -->
                <el-button
                  type="danger"
                  size="small"
                  @click="clearKeywords"
                  :disabled="!keywords.length"
                  @mousedown.native="pressedClear = true"
                  @mouseup.native="pressedClear = false"
                  @mouseleave.native="pressedClear = false"
                  :style="{
                    transition: 'all 0.2s ease',
                    transform: pressedClear ? 'scale(0.98)' : 'scale(1)'
                  }"
                >清空关键词</el-button>
              </div>
            </div>






            <!-- 已提取关键词 -->
            <div class="control-section mt-20">
              <h4>已提取脱敏关键词类别</h4>
              <div class="keyword-tags">
                <el-tag
                  v-for="(kw, index) in keywords"
                  :key="index"
                  type="success"
                  closable
                  @close="removeKeyword(kw)"
                  class="mr-5 mb-5"
                >{{ kw }}</el-tag>
                <span v-if="!keywords.length" class="text-muted">无已提取类别</span>
              </div>
            </div>

            <!-- 常用关键词 -->
            <div class="control-section mt-20">
              <h4>常用脱敏关键词</h4>
              <div class="keyword-tags">
                <el-tag
                  v-for="(kw, index) in commonKeywords"
                  v-if="!keywords.includes(kw)"
                  :key="'common-'+index"
                  type="info"
                  class="mr-5 mb-5 clickable"
                  @click="toggleKeyword(kw)"
                >{{ kw }}</el-tag>
              </div>
            </div>
          </el-card>

          <el-card class="box-card" style="margin-top: 20px; height: 188px;">
             <div slot="header">
           <span style="font-size: 20px; font-weight: bold;">脱敏算法选择</span>
           </div>

            <div>
              <el-tag
                v-for="mode in algorithmModes"
                :key="mode"
                :type="mode === selectedAlgorithm ? 'success' : 'info'"
                @click="selectAlgorithm(mode)"
                style="margin: 5px; cursor: pointer;"
              >
                 {{ mode }}
              </el-tag>
            </div>
          </el-card>
        </el-col>

        <!-- 右侧文本处理区 -->
        <el-col :span="14">
          <el-card class="box-card">
             <div slot="header">
           <span style="font-size: 20px; font-weight: bold;">文本处理区</span>
           </div>


            <!-- 输入 -->
            <div class="text-box">
              <h4>输入待处理文本</h4>



              <el-input
                type="textarea"
                :rows="15"
                :placeholder="uploadedFileName ? '' : '请粘贴需要脱敏的文本内容'"
                v-model="inputText"
                resize="none"
                class="input-area"
              />

              <p v-if="uploadedFileName" style="color: #409EFF; font-size: 13px; display: flex; align-items: center; gap: 8px;">
                已导入文件：{{ uploadedFileName }}
                <el-button
                  type="danger"
                  size="mini"
                  icon="el-icon-delete"
                  @click="removeUploadedFile"
                  style="margin-left: 8px; padding: 2px 8px;"
                >删除</el-button>
              </p>


              <!-- 横向容器：按钮 + 小字 -->
              <div style="display: flex; align-items: center; gap: 10px; margin-top: 10px;">
                <el-upload
                  :show-file-list="false"
                  accept=".pdf,.doc,.docx,.txt"
                  action=""
                  :auto-upload="false"
                  :on-change="handleUpload"
                >
                  <el-button
                    size="small"
                    type="primary"
                    @mousedown.native="pressedImport = true"
                    @mouseup.native="pressedImport = false"
                    @mouseleave.native="pressedImport = false"
                    
                    :style="{
                      backgroundColor: pressedImport ? '#b8cbd4' : '#4f789c',
                      borderColor: pressedImport ? '#b8cbd4' : '#4f789c',
                      color: '#fff',
                      transition: 'all 0.2s ease',
                      transform: pressedImport ? 'scale(0.97)' : 'scale(1)'
                    }"
                  >
                    导入文件
                  </el-button>

                
                  
                </el-upload>

              <span style="font-size: 13px; color: #666;">支持 pdf、word、txt 格式</span>
            </div>
          </div>
          <!-- </el-card>
        </el-col> -->

              <!-- 文件名列表展示区 -->
              <!-- <div v-if="uploadedFiles.length" style="margin-top: 10px; font-size: 13px; color: #444;">
                <div v-for="(file, index) in uploadedFiles" :key="index">
                  {{ file.name }}
                </div>
              </div> -->



            <!-- 输出 -->
            <!-- <div class="text-box mt-20">
              <h4>输出处理后文本</h4>
              <el-input
                type="textarea"
                v-model="outputText"
                :rows="10"
                resize="none"
                class="output-area"
              />
              <div class="highlighted-output mt-10" v-html="highlightedOutputHtml"></div>
            </div> -->



          <!-- 输出+按钮+实体下拉框区域 -->
          <div class="output-entity-container" style="display: flex; gap: 20px; align-items: flex-start;">
            
            <!-- 左半部分：输出框 + 按钮 -->
            <div class="output-section" style="flex: 1;">
              <div class="text-box mt-20">
                <h4>输出处理后文本</h4>
                <el-input
                  type="textarea"
                  v-model="outputText"
                  :rows="10"
                  resize="none"
                  class="output-area"
                  style="width: 100%;"
                />
                <!-- <div class="highlighted-output mt-10" v-html="highlightedOutputHtml"></div> -->
              </div>

              <!-- 操作按钮 -->
              <div class="button-row mt-20" style="display: flex; gap: 10px;">
                <el-button
                  type="primary"
                  :disabled="!inputText || loading"
                  @click="handleDesensitize"
                  @mousedown.native="pressedDesensitize = true"
                  @mouseup.native="pressedDesensitize = false"
                  @mouseleave.native="pressedDesensitize = false"
                  :style="{
                    backgroundColor: pressedExtract ? '#98b0a3' : (hoverExtract ? '#3e7b5a' : '#2e5c42'),
                    borderColor: pressedExtract ? '#ecf4f0' : (hoverExtract ? '#3e7b5a' : '#2e5c42'),
                    color: '#fff',
                    transition: 'all 0.2s ease',
                    transform: pressedDesensitize ? 'scale(0.97)' : 'scale(1)'
                  }"
                >
                  <span v-if="loading">处理中...</span>
                  <span v-else>开始脱敏</span>
                </el-button>

                <el-button
                  type="info"
                  @click="handleCopy"
                  :disabled="!outputText"
                  :style="{
                    backgroundColor: '#fff',
                    borderColor: 'grey',
                    color: 'black',
                    transition: 'all 0.2s ease',
                    transform: pressedCopy ? 'scale(0.97)' : 'scale(1)'
                  }"
                >
                  复制结果
                </el-button>

                <el-button
                  type="warning"
                  @click="handleExport"
                  :disabled="!outputText"
                  :style="{
                    backgroundColor: pressedExport ? '#6b90ad' : '#4f789c',
                    borderColor: pressedExport ? '#6b90ad' : '#4f789c',
                    color: '#fff',
                    transition: 'all 0.2s ease',
                    transform: pressedExport ? 'scale(0.97)' : 'scale(1)'
                  }"
                >
                  导出结果
                </el-button>
              </div>

              <!-- 进度条区域 -->
              <div v-if="loading" class="progress-section mt-20">
                <div class="progress-info">
                  <span class="progress-text">{{ progressText }}</span>
                  <el-button
                    type="danger"
                    size="mini"
                    icon="el-icon-close"
                    circle
                    @click.stop="interruptProcess"
                    class="interrupt-btn"
                    style="z-index: 1000;"
                    title="点击中断处理"
                  />
                </div>
                <el-progress 
                  :percentage="progressPercentage" 
                  :stroke-width="8"
                  :show-text="false"
                  :color="progressColor"
                />
              </div>

            </div>

            <!-- 右半部分：实体替换 -->
            <div class="entity-section" style="flex: 1;">
              <!-- 将标题挪到框外，与左侧对齐 -->
              <div style="margin-top: 20px;">
                <h4>实体替换结果</h4>
              </div>

              <!-- 表格区域单独包裹 -->
              <div class="entity-table-wrapper">
                <el-table
                  :data="entityPairs.slice(0, 3)"
                  border
                  style="width: 100%;"
                  size="small"
                >
                  <el-table-column label="处理前" prop="before" />
                  <el-table-column label="处理后" prop="after" />
                </el-table>
                <div style="text-align: right; margin-top: 1px;">
                  <el-button type="text" @click="dialogVisible = true">更多</el-button>
                </div>
              </div>
            </div>



            <!-- Dialog 弹窗 -->
            <el-dialog title="全部实体替换列表" :visible.sync="dialogVisible" width="60%">
              <el-table
                :data="entityPairs"
                border
                style="width: 100%;"
                size="medium"
                max-height="400"
              >
                <el-table-column label="处理前" prop="before" />
                <el-table-column label="处理后" prop="after" />
              </el-table>
              <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">关闭</el-button>
              </span>
            </el-dialog>            

          </div>

          </el-card>
        </el-col>
      </el-row>
    </div>
          


    <div v-if="loading" class="loading-spinner">
      <el-spinner size="large" />
    </div>
    <!-- 外层根元素 END -->
  </div>
</template>



<script>
import { processDesensitize } from '@/utils/daili'

export default {
  data() {
    return {
      inputText: '',
      uploadedFileName: '', // 新增变量：已导入文件名
      outputText: '',

      uploadedFileContent: null,
      uploadedFileName: '',
    

      //新增：
      dialogVisible: false,
      entityPairs: [
        { before: '张三', after: '[姓名]' },
        { before: '2024年9月21日', after: '[时间]' },
        { before: '梅花西路128号', after: '[地点]' },
        { before: '李海欣', after: '[姓名]' },
        { before: '大米集团', after: '[工作单位]' },
        { before: '13812345678', after: '[电话号码]' },
        { before: 'zhangsan@example.com', after: '[邮箱]' },
      ],


      pressedImport: false,
      uploadedFiles: [] , // 存储上传文件列表

      hoverExtract: false,
      pressedExtract: false,
      pressedClear: false,
      pressedImport: false,
      pressedDesensitize: false,
      pressedCopy: false,
      pressedExport: false,

      loading: false,
      // 进度条相关变量
      progressPercentage: 0,
      progressText: '',
      progressColor: '#409EFF',
      currentStage: 0,
      // 中断相关变量
      isInterrupted: false,
      abortController: null,
      inputText: `2024年5月8日，上市公司大米集团市场部经理刘丽就大米集团在新能源汽车领域未来的发展与比克里能源有限公司总经理李海欣在海珠市喜来登大酒店进行会谈，双方会中达成合作共识，比克里能源有限公司将承担起大米集团整车制作过程中的关键能源技术支持和材料提供工作。会后双方前往位于海珠桂园区的大米集团新能源汽车研发总部进行参观，李海欣经理表示看好未来的发展前景`,
      outputText: '',
      exampleText: "张三2024年9月21日在梅花西路128号与李四签订两百块的合作协议[金额'两百块']",
      keywords: [],
      selectedKeywords: [],
      commonKeywords: ['姓名', '时间', '地点', '工作单位', '家庭住址', '电话号码', '邮箱'],
      algorithmModes: ['关键词模糊', '同义替换'],
      patternMap: {
        '关键词模糊': 1,
        '同义替换': 2,
        '基于示例学习': 3
      },
      selectedAlgorithm: '规则匹配',
      defaultDemoData: {
        姓名: {
          原始语句: "张三在会议中提出了建议。",
          关注的词: "张三",
          输出: "##Yes##,在给定的文本里面,张三是一个人的名字,因此它属于姓名类型"
        },
        时间: {
          原始语句: "会议安排在2024年9月21日举行。",
          关注的词: "2024年9月21日",
          输出: "##Yes##,在给定的文本里面,2024年9月21日是具体时间,属于时间类型"
        },
        地点: {
          原始语句: "他居住在梅花西路128号。",
          关注的词: "梅花西路128号",
          输出: "##Yes##,在给定的文本里面,梅花西路128号是一个地址,属于地点类型"
        },
        工作单位: {
          原始语句: "李四在华为公司担任工程师。",
          关注的词: "华为公司",
          输出: "##Yes##,在给定的文本里面,华为公司是工作单位的名称,因此它属于工作单位类型"
        },
        家庭住址: {
          原始语句: "他的家庭住址是成都市武侯区玉林南路66号。",
          关注的词: "成都市武侯区玉林南路66号",
          输出: "##Yes##,在给定的文本里面,成都市武侯区玉林南路66号是一个具体的住址,属于家庭住址类型"
        },
        电话号码: {
          原始语句: "请拨打13812345678联系他。",
          关注的词: "13812345678",
          输出: "##Yes##,在给定的文本里面,13812345678是一个手机号,属于电话号码类型"
        },
        邮箱: {
          原始语句: "你可以发邮件到zhangsan@example.com。",
          关注的词: "zhangsan@example.com",
          输出: "##Yes##,在给定的文本里面,zhangsan@example.com是一个邮箱地址,属于邮箱类型"
        }
      }
    };
  },

  created() {
    axios.interceptors.request.use(config => {
      console.log('🚀 发送请求到后端：', config);
      return config;
    }, error => Promise.reject(error));

    axios.interceptors.response.use(response => {
      console.log('✅ 后端响应：', response);
      return response;
    }, error => Promise.reject(error));
  },

  methods: {

  //     handleUpload(file) {
  //   return new Promise((resolve, reject) => {
  //     const reader = new FileReader();
  //     reader.onload = (e) => {
  //       this.inputText = e.target.result;
  //       this.uploadedFileName = file.name; // 存储上传的文件名
  //       console.log('handleUpload 被调用了:', file.name); // ✅ debug log
  //       this.$message.success('导入成功')
  //       resolve(false); // 阻止默认上传
  //     };
  //     reader.onerror = (e) => {
  //       this.$message.error('读取文件失败');
  //       console.log('handleUpload 调用失败:'); 
  //       reject(false);
  //     };
  //     reader.readAsText(file, 'utf-8');
  //   });
  // },
  handleUpload(uploadFile) {
  const file = uploadFile.raw || uploadFile.file;
  const reader = new FileReader();

  reader.onload = () => {
  const base64Content = reader.result.split(',')[1];

  this.uploadedFileName = file.name;
  this.uploadedFileContent = {
    filename: file.name,
    content: base64Content,
    content_type: file.type || 'application/octet-stream'
  };

  this.$message.success('✅ 文件读取成功：' + file.name);
  console.log("file 字段：", this.uploadedFileContent);

  };

  reader.onerror = (e) => {
    this.$message.error('❌ 文件读取失败');
    console.error(e);
  };

  reader.readAsDataURL(file);
},


    handleFileChange(file, fileList) {
    this.uploadedFiles = fileList.map(item => item.raw || item); // 存储上传的文件列表
  },

    // 新增差异高亮函数，只改颜色，黄色字显示差异，黑色字显示相同
  highlightDiff(resource, result) {
    if (!resource || !result) return result;

    let i = 0,
      j = 0;
    const resLen = resource.length;
    const resultLen = result.length;
    let highlighted = "";

    while (i < resLen && j < resultLen) {
      if (resource[i] === result[j]) {
        highlighted += `<span style="color: black">${result[j]}</span>`;
        i++;
        j++;
      } else {
        highlighted += `<span style="color: yellow">${result[j]}</span>`;
        j++;
      }
    }

    // result多余部分算差异
    while (j < resultLen) {
      highlighted += `<span style="color: yellow">${result[j]}</span>`;
      j++;
    }

    return highlighted;
  },

      // // 新增：提取实体对
      // extractEntityPairs(original, desensitized) {
      //   const pairs = [];
      //   let i = 0, j = 0;
      //   let origBuf = '', desBuf = '';

      //   while (i < original.length && j < desensitized.length) {
      //     if (original[i] === desensitized[j]) {
      //       i++; j++;
      //     } else {
      //       // 开始差异区域
      //       origBuf = '';
      //       desBuf = '';
      //       while (i < original.length && j < desensitized.length && original[i] !== desensitized[j]) {
      //         origBuf += original[i];
      //         desBuf += desensitized[j];
      //         i++; j++;
      //       }

      //       // 忽略过短的差异
      //       if (origBuf.length > 0 && desBuf.length > 0 && origBuf !== desBuf) {
      //         pairs.push({ before: origBuf, after: desBuf });
      //       }
      //     }
      //   }

      //   return pairs;
      // },

    async handleDesensitize() {
      this.loading = true;
      this.isInterrupted = false;
      this.currentStage = 0;
      this.progressPercentage = 0;
      this.progressText = '准备开始处理...';
      this.progressColor = '#409EFF';
      
      // 创建AbortController用于中断请求
      this.abortController = new AbortController();
      
      try {
        // 第一阶段：准备数据 (0-25%)
        this.currentStage = 1;
        this.progressText = '正在准备数据...';
        this.progressPercentage = 0;
        
        // 检查是否被中断
        if (this.isInterrupted) {
          throw new Error('用户中断了处理');
        }
        
        this.parseExample();
        const demos = [
          ...this.generateDynamicDemos(),
          ...this.getSelectedPresetDemos()
        ];

        // 构造基础请求体
        const requestData = {
          entity_type: this.keywords.join('、'),
          demos: demos,
          patten: this.patternMap[this.selectedAlgorithm],
          keywords: this.keywords  // 添加关键词字段
        };

        // 判断是否使用 uploadedFileContent
        if (this.uploadedFileContent) {
          requestData.file = this.uploadedFileContent;
          console.log("📦 发送文件内容：", this.uploadedFileContent);
        } else if (this.inputText && this.inputText.trim().length > 0) {
          requestData.text = this.inputText.trim();
          console.log("✏️ 发送用户手写文本：", this.inputText.trim());
        } else {
          this.$message.warning("请先输入文本或上传文件！");
          this.loading = false;
          return;
        }

        // 模拟上传进度 (0-25%)
        await this.simulateProgress(0, 25, 500);
        
        // 检查是否被中断
        if (this.isInterrupted) {
          throw new Error('用户中断了处理');
        }
        
        // 第二阶段：后端处理 (25-100%)
        this.currentStage = 2;
        this.progressText = '正在处理数据...';
        this.progressColor = '#67C23A';
                
        // 在第651行附近，替换API调用
        // const res = await axios.post('/api/process', requestData, {
        //   headers: {
        //     'Content-Type': 'application/json'
        //   },
        //   signal: this.abortController.signal
        // });

        const res = await processDesensitize(requestData);

        // 检查是否被中断
        if (this.isInterrupted) {
          throw new Error('用户中断了处理');
        }

        // 模拟后端处理进度 (25-95%)
        await this.simulateProgress(25, 95, 1000);
        
        // 检查是否被中断
        if (this.isInterrupted) {
          throw new Error('用户中断了处理');
        }
        
        // 第三阶段：完成 (95-100%)
        this.currentStage = 3;
        this.progressText = '处理完成';
        this.progressColor = '#67C23A';
        this.progressPercentage = 100;

        this.outputText = res.data.result;
        this.entityPairs = res.data.word_dic
          ? Object.entries(res.data.word_dic).map(([before, after]) => ({ before, after }))
          : [];

        this.$message.success('脱敏成功');
        
        // 延迟关闭进度条
        setTimeout(() => {
          this.loading = false;
          this.currentStage = 0;
          this.progressPercentage = 0;
          this.isInterrupted = false;
        }, 1000);
        
      } catch (e) {
        console.error('❌ 请求失败：', e);
        
        if (this.isInterrupted) {
          this.progressText = '已中断处理';
          this.progressColor = '#E6A23C';
          this.$message.warning('处理已中断');
        } else {
          this.progressText = '处理失败';
          this.progressColor = '#F56C6C';
          this.$message.error('处理失败');
        }
        
        // 延迟关闭进度条
        setTimeout(() => {
          this.loading = false;
          this.currentStage = 0;
          this.progressPercentage = 0;
          this.isInterrupted = false;
        }, 2000);
      }
    },

    selectAlgorithm(mode) {
      this.selectedAlgorithm = mode;
    },

    generateDynamicDemos() {
      const keywordPattern = /\[([^\]]+?)'([^']+?)'\]/g;
      let match;
      const dynamicDemos = [];

      while ((match = keywordPattern.exec(this.exampleText)) !== null) {
        const entityType = match[1].trim();
        const mention = match[2].trim();
        const rawSentence = this.exampleText.replace(`[${entityType}'${mention}']`, mention);

        dynamicDemos.push({
          原始语句: rawSentence,
          关注的词: mention,
          输出: `##Yes##,在给定的文本里面,${mention}是一个${entityType},属于${entityType}类型`
        });
      }

      return dynamicDemos;
    },

    getSelectedPresetDemos() {
      return this.selectedKeywords.map(kw => ({
        原始语句: this.defaultDemoData[kw]?.原始语句 || `示例${kw}`,
        关注的词: this.defaultDemoData[kw]?.关注的词 || `示例${kw}`,
        输出: this.defaultDemoData[kw]?.输出 || `示例${kw}的脱敏输出`
      }));
    },

    parseExample() {
      const keywordPattern = /\[([^\]]+?)'([^']+?)'\]/g;
      let match;
      const extracted = new Set(this.keywords);

      while ((match = keywordPattern.exec(this.exampleText)) !== null) {
        const entityType = match[1].trim();
        if (!extracted.has(entityType)) {
          extracted.add(entityType);
        }
      }

      this.keywords = Array.from(extracted);
    },

    toggleKeyword(kw) {
      if (this.keywords.includes(kw)) {
        this.keywords = this.keywords.filter(k => k !== kw);
      } else {
        this.keywords.push(kw);
      }
    },

    clearKeywords() {
      this.keywords = [];
    },

    removeKeyword(kw) {
      this.keywords = this.keywords.filter(k => k !== kw);
    },

  //  handleUpload(file) {
   //   const reader = new FileReader();
  //    reader.onload = (e) => {
   //     this.inputText = e.target.result;
  //    };
  //    reader.readAsText(file.raw);
  //    return false;
 //   },

    handleCopy() {
      navigator.clipboard.writeText(this.outputText).then(() => {
        this.$message.success('已复制到剪贴板');
      });
    },

    handleExport() {
      const blob = new Blob([this.outputText], { type: 'text/plain;charset=utf-8' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = '脱敏结果.txt';
      link.click();
    },
    removeUploadedFile() {
      this.uploadedFileName = '';
      this.uploadedFileContent = null;
    },

    // 中断处理方法
    interruptProcess() {
      console.log('中断按钮被点击');
      
      // 立即显示消息确认按钮被点击
      this.$message.info('中断按钮被点击');
      
      this.isInterrupted = true;
      
      // 中断HTTP请求
      if (this.abortController) {
        this.abortController.abort();
        console.log('HTTP请求已中断');
      }
      
      // 立即更新UI状态
      this.progressText = '正在中断...';
      this.progressColor = '#E6A23C';
      
      console.log('用户中断了处理');
      
      // 立即关闭loading状态
      setTimeout(() => {
        this.loading = false;
        this.currentStage = 0;
        this.progressPercentage = 0;
        this.isInterrupted = false;
        this.$message.warning('处理已中断');
      }, 500);
    },

    // 模拟进度条进度
    simulateProgress(start, end, duration) {
      return new Promise((resolve, reject) => {
        const steps = 20;
        const increment = (end - start) / steps;
        const interval = duration / steps;
        let current = start;
        
        const timer = setInterval(() => {
          // 检查是否被中断
          if (this.isInterrupted) {
            clearInterval(timer);
            console.log('进度模拟被中断');
            reject(new Error('用户中断了处理'));
            return;
          }
          
          current += increment;
          this.progressPercentage = Math.min(current, end);
          
          if (current >= end) {
            clearInterval(timer);
            resolve();
          }
        }, interval);
      });
    }
  }
}
</script>







<style scoped>
.container {
  padding: 20px;
  font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, "Microsoft YaHei", sans-serif;
  background-color:#ecf4f0;
}

.mt-10 {
  margin-top: 10px;
}

.mt-20 {
  margin-top: 20px;
}

.text-box {
  margin-bottom: 10px;
}

.input-area,
.output-area {
  border: 1px solid #dcdfe6;
  border-radius: 6px;
  padding: 10px;
  font-size: 14px;
  line-height: 1.6;
  font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, "Microsoft YaHei", sans-serif;
  background-color: #f9f9f9;
  height: 160px;
  overflow-y: auto;
}

.input-area:hover,
.output-area:hover {
  border-color: #409EFF;
}

.keyword-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.clickable:hover {
  transform: scale(1.05);
  cursor: pointer;
}

.entity-table-wrapper {
  margin-top: 20px;
  padding: 10px;
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 6px;
}

/* 进度条样式 */
.progress-section {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 20px;
  margin-top: 20px;
}

.progress-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  position: relative;
  z-index: 10;
}

.progress-text {
  font-size: 14px;
  color: #606266;
  font-weight: 500;
}

.interrupt-btn {
  transition: all 0.3s ease;
  cursor: pointer !important;
  pointer-events: auto !important;
  position: relative;
  z-index: 1000;
}

.interrupt-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 2px 8px rgba(245, 108, 108, 0.3);
}

.interrupt-btn:active {
  transform: scale(0.95);
}
</style>