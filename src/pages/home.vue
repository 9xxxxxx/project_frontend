<!-- src/views/Home.vue -->
<template>
  <div class="min-h-screen flex  justify-center bg-gray-50 p-6">
    <div class="w-full max-w-4xl bg-white p-10 rounded-2xl shadow-lg">
      <!-- Logo 和标题 -->
      <div class="text-center mb-10">
        <img src="/logo.png" alt="Logo" class="mx-auto h-16 mb-4" />
        <h1 class="text-3xl font-bold text-blue-600 mb-2">
          欢迎来到数据可视化平台
        </h1>
        <p class="text-sm text-gray-500">
          基于 Vue 3 + TailwindCSS 构建的现代前端系统
        </p>
      </div>

      <!-- 功能卡片 -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div
          class="bg-blue-50 p-6 rounded-xl shadow hover:shadow-md transition"
        >
          <h2 class="text-lg font-semibold text-blue-700 mb-2">📊 数据报表</h2>
          <p class="text-gray-600 text-sm mb-3">
            查看详细的运营指标、数据趋势与图表洞察。
          </p>
          <router-link
            to="/reports"
            class="text-sm text-blue-500 hover:underline"
            >进入模块 →</router-link
          >
        </div>
        <div
          class="bg-green-50 p-6 rounded-xl shadow hover:shadow-md transition"
        >
          <h2 class="text-lg font-semibold text-green-700 mb-2">👥 用户管理</h2>
          <p class="text-gray-600 text-sm mb-3">
            管理系统用户、权限及行为记录。
          </p>
          <router-link
            to="/users"
            class="text-sm text-green-500 hover:underline"
            >进入模块 →</router-link
          >
        </div>
        <div class="bg-red-50 p-6 rounded-xl shadow hover:shadow-md transition">
          <h2 class="text-lg font-semibold text-red-700 mb-2">🚨 异常监控</h2>
          <p class="text-gray-600 text-sm mb-3">
            实时监控生产异常，快速排查与分析。
          </p>
          <router-link
            to="/monitor"
            class="text-sm text-red-500 hover:underline"
            >进入模块 →</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// 页面逻辑
</script>
