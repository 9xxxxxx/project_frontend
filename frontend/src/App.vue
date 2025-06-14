<template>
  <!-- 使用 NConfigProvider 包裹，为 naive-ui 组件提供配置环境 -->
  <NConfigProvider>

      <!-- 页面内容区域 -->
      <header>
        <router-view />
      </header>

      <!-- 页脚 -->
      <footer class="bg-white text-center text-sm text-gray-400 py-4 shadow-inner">
        © 2025 我的 Vue 项目 · 使用 TailwindCSS 构建
      </footer>

  </NConfigProvider>
</template>






<script setup>
import { NConfigProvider } from 'naive-ui';
// 若需要在当前组件内使用以下组件，可在模板合适位置添加使用
import ShowData from "./components/ShowData.vue";
import ShowTable from "./components/ShowTable.vue";
</script>

<style>
/* 可根据需要引入 naive-ui 基础样式，比如：
  @import 'naive-ui/lib/styles/index.css'; 
  不过 vite + vue3 + naive-ui 组合下，也可通过自动按需引入样式（配置 babel 插件等方式），具体看项目实际配置 
*/
</style>