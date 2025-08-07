import axios from 'axios'

// 创建一个新的axios实例
const service = axios.create({
  baseURL: 'http://114.132.160.53:12345/process', // 你的后端地址
  timeout: 500000000 // 请求超时时间
})


// 定义 processDesensitize 函数，用于发送请求
export const processDesensitize = async (data) => {
    try {
      const response = await service.post('/desensitize', data);  // 发送脱敏请求
      return response;  // 返回响应数据
    } catch (error) {
      throw error;  // 错误抛出，交由调用方处理
    }
  }


// 请求拦截器

service.interceptors.request.use(
  config => {
    // 如果需要添加 token 或其他 header，在这里处理
    // 如果需要其他设置，可以在这里做额外配置
    return config
  },
  error => {
    console.log('请求错误', error) // 调试
    return Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  response => {
    const res = response.data

    // 这里你可以根据后端的返回状态码做相应的处理
    if (res.code !== 20000) {
      console.error('请求错误', res.message || 'Error')
      return Promise.reject(new Error(res.message || 'Error'))
    } else {
      return res
    }
  },
  error => {
    console.log('响应错误', error)
    return Promise.reject(error)
  }
)

export default service