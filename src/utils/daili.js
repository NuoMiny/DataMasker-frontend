import axios from 'axios'

// 创建一个新的axios实例
const service = axios.create({
  baseURL: 'http://114.132.160.53:12345', // 你的后端地址
  timeout: 500000000 // 请求超时时间
})
// const service = axios.create({
//   baseURL: 'http://localhost:12345', // 改为本地地址，去掉/process
//   timeout: 500000000 // 请求超时时间
// })

// 定义 processDesensitize 函数，用于发送请求
export const processDesensitize = async (data) => {
  try {
    const response = await service.post('/process', data); // 明确指定/process路径
    return response;
  } catch (error) {
    throw error;
  }
}


// 请求拦截器

service.interceptors.request.use(
  config => {
    console.log('🚀 发送请求到:', config.baseURL + config.url);
    console.log('📦 请求数据:', config.data);
    return config
  },
  error => {
    console.log('❌ 请求错误', error)
    return Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  response => {
    console.log('✅ 后端响应:', response.data);
    return response; // 直接返回response，让调用者处理
  },
  error => {
    console.log('❌ 响应错误', error)
    return Promise.reject(error)
  }
)

export default service