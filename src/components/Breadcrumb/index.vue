\<template>
  <div class="app-breadcrumb-wrapper">
    <img
      class="breadcrumb-avatar"
      :src="require('@/assets/DataMasker.png')"
      alt="logo"
    />
    <el-breadcrumb class="app-breadcrumb" separator="/">
      <transition-group name="breadcrumb">
        <el-breadcrumb-item v-for="(item,index) in levelList" :key="item.path">
          <span v-if="item.redirect==='noRedirect'||index==levelList.length-1" class="no-redirect">{{ item.meta.title }}</span>
          <a v-else @click.prevent="handleLink(item)">{{ item.meta.title }}</a>
        </el-breadcrumb-item>
      </transition-group>
    </el-breadcrumb>
  </div>
</template>

<script>
import pathToRegexp from 'path-to-regexp'

export default {
  data() {
    return {
      levelList: null
    }
  },
  watch: {
    $route() {
      this.getBreadcrumb()
    }
  },
  created() {
    this.getBreadcrumb()
  },
  methods: {
    getBreadcrumb() {
      let matched = this.$route.matched.filter(item => item.meta && item.meta.title)
      const first = matched[0]

      if (!this.isDashboard(first)) {
        matched = [{ path: '/dashboard', meta: { title: '首页' }}].concat(matched)
      }

      this.levelList = matched.filter(item => item.meta && item.meta.title && item.meta.breadcrumb !== false)
    },
    isDashboard(route) {
      const name = route && route.name
      return name && name.trim().toLowerCase() === 'dashboard'
    },
    pathCompile(path) {
      const { params } = this.$route
      const toPath = pathToRegexp.compile(path)
      return toPath(params)
    },
    handleLink(item) {
      const { redirect, path } = item
      this.$router.push(redirect || this.pathCompile(path))
    }
  }
}
</script>

<style lang="scss" scoped>
.app-breadcrumb-wrapper {
  display: flex;
  align-items: center;
  height: 90px; // container高度
  padding: 0 20px;
  background-color: #fff;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);

  .breadcrumb-avatar {
    height: 100%;       // 图片等于 container 高度
    width: auto;              // 保持宽高比，不拉伸
    object-fit: contain;      // 保证完整展示
    margin-right: 16px;
    border-radius: 0;         // 取消圆形
  }
}




.el-breadcrumb-item {
  line-height: 60px;
}

.app-breadcrumb.el-breadcrumb {
  display: inline-block;
  font-size: 14px;
  line-height: 60px;

  .el-breadcrumb__inner,
  .el-breadcrumb__inner a,
  .no-redirect { // ✅ 添加 no-redirect 样式
    font-size: 18px;
  }

  .no-redirect {
    color: #97a8be;
    cursor: default;
  }
}
</style>