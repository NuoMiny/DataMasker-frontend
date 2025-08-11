'use strict'
const path = require('path')
const defaultSettings = require('./src/settings.js')

function resolve(dir) {
  return path.join(__dirname, dir)
}

const name = defaultSettings.title || 'vue Admin Template' // 页面标题
const port = process.env.port || process.env.npm_config_port || 9528 // 开发端口号

module.exports = {
  transpileDependencies: [],

  publicPath: '/',
  outputDir: 'dist',
  assetsDir: 'static',
  lintOnSave: process.env.NODE_ENV === 'development',
  productionSourceMap: false,

  devServer: {
    port: port,
    open: true,
    proxy: {
      '/api': {
        target: 'http://localhost:12345',
        changeOrigin: true,
        pathRewrite: { '^/api': '' }
      }
    }
  },

  configureWebpack: {
    name: name,
    resolve: {
      alias: {
        '@': resolve('src')
      }
    }
  },

  chainWebpack(config) {
    // 仅当 preload 插件存在时才去修改
    if (config.plugins.has('preload')) {
      config.plugin('preload').tap(options => {
        options[0].fileBlacklist.push(/\.map$/, /hot-update\.js$/, /runtime\..*\.js$/)
        options[0].include = 'initial'
        return options
      })
    }

    // 删除 prefetch 插件
    config.plugins.delete('prefetch')

    // 设置 SVG 图标处理规则
    config.module
      .rule('svg')
      .exclude.add(resolve('src/icons'))
      .end()

    config.module
      .rule('icons')
      .test(/\.svg$/)
      .include.add(resolve('src/icons'))
      .end()
      .use('svg-sprite-loader')
      .loader('svg-sprite-loader')
      .options({
        symbolId: 'icon-[name]'
      })
      .end()

    // 生产环境配置优化
    config.when(process.env.NODE_ENV !== 'development',
      config => {
        config
          .plugin('ScriptExtHtmlWebpackPlugin')
          .after('html')
          .use('script-ext-html-webpack-plugin', [{
            inline: /runtime\..*\.js$/
          }])
          .end()

        config.optimization.splitChunks({
          chunks: 'all',
          cacheGroups: {
            libs: {
              name: 'chunk-libs',
              test: /[\\/]node_modules[\\/]/,
              priority: 10,
              chunks: 'initial'
            },
            elementUI: {
              name: 'chunk-elementUI',
              priority: 20,
              test: /[\\/]node_modules[\\/]_?element-ui(.*)/
            },
            commons: {
              name: 'chunk-commons',
              test: resolve('src/components'),
              minChunks: 3,
              priority: 5,
              reuseExistingChunk: true
            }
          }
        })

        config.optimization.runtimeChunk('single')
      }
    )
  }
}