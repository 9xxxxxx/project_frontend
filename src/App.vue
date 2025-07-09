<template>
    <NConfigProvider>
      <n-message-provider>
        <n-loading-bar-provider>
          <MyHeader />
          <main>
            <router-view />
          </main>
          <footer class="bg-white text-center text-sm text-gray-400 py-4 shadow-inner">
            © 2025 我的 Vue 项目 · 使用 TailwindCSS 构建
          </footer>
        </n-loading-bar-provider>
      </n-message-provider>
    </NConfigProvider>
</template>

<script setup>
import { NConfigProvider, NMessageProvider, NLoadingBarProvider } from 'naive-ui';  
import ShowData from "./components/ShowData.vue";
import ShowTable from "./components/ShowChart.vue";
import any from './components/any.vue';
import MyHeader from './components/MyHeader.vue';
import { RouterView } from 'vue-router';
</script>

<style></style>