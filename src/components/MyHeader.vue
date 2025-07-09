<template>
  <header class="bg-gradient-to-r from-blue-700 via-purple-700 to-pink-600 text-white shadow-lg sticky top-0 z-50">
    <div class="container mx-auto px-4 md:px-10 py-4 flex justify-between items-center relative">
      <!-- Logo -->
      <div class="flex items-center">
        <a href="/" class="flex items-center text-2xl font-bold tracking-wide hover:text-blue-200 transition">
          <svg class="w-8 h-8 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M7 12l3-3m0 0l3 3m-3-3v8m0-13a9 9 0 110 18 9 9 0 010-18z"></path>
          </svg>
          数据洞察平台
        </a>
      </div>

      <!-- Desktop Menu -->
      <nav class="hidden md:flex relative">
        <div class="flex space-x-15 ">
          <div v-for="item in menuItems" :key="item.name" class="group relative flex-shrink-0 ml-6">
            <a :href="item.link" class="text-lg font-medium transition duration-300">
              {{ item.name }}
            </a>
            <span
              class="absolute left-0 bottom-0 w-full h-0.5 bg-yellow-400 scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left"></span>
          </div>
        </div>
      </nav>


      <!-- Right -->
      <div class="flex items-center space-x-4">
        <template v-if="!isLoggedIn">
          <a href="/login"
            class="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-md text-base font-medium transition hidden lg:inline-block">登录</a>
          <a href="/register"
            class="border border-blue-200 text-blue-200 hover:bg-blue-600 hover:text-white px-4 py-2 rounded-md text-base font-medium transition hidden lg:inline-block">注册</a>
        </template>

        <template v-else>
          <div class="relative group">
            <button class="flex items-center space-x-2 focus:outline-none">
              <img src="/avatar.png" alt="User Avatar" class="w-9 h-9 rounded-full border-2 border-white">
              <span class="hidden md:inline text-lg font-medium">哈吉甘</span>
              <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </button>

            <div
              class="absolute right-0 mt-3 w-48 bg-white text-gray-700 rounded-md shadow-lg py-1 opacity-0 group-hover:opacity-100 group-hover:translate-y-2 transform transition-all duration-300 z-50 pointer-events-none group-hover:pointer-events-auto">
              <a href="/profile" class="block px-4 py-2 hover:bg-gray-100">个人中心</a>
              <a href="/account-settings" class="block px-4 py-2 hover:bg-gray-100">账号设置</a>
              <div class="border-t my-1"></div>
              <button @click="logout" class="w-full text-left px-4 py-2 text-red-500 hover:bg-gray-100">登出</button>
            </div>
          </div>
        </template>

        <!-- Mobile button -->
        <button class="md:hidden focus:outline-none" @click="toggleMobileMenu">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!isMobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"></path>
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12">
            </path>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <nav v-if="isMobileMenuOpen" class="md:hidden bg-blue-800 py-4">
      <a v-for="item in menuItems" :key="item.name" :href="item.link"
        class="block px-6 py-3 text-lg font-medium text-white hover:bg-blue-700 transition" @click="closeMobileMenu">{{
          item.name }}</a>

      <template v-if="!isLoggedIn">
        <hr class="my-2 border-blue-700">
        <a href="/login" class="block px-6 py-3 text-lg font-medium text-white hover:bg-blue-700"
          @click="closeMobileMenu">登录</a>
        <a href="/register" class="block px-6 py-3 text-lg font-medium text-white hover:bg-blue-700"
          @click="closeMobileMenu">注册</a>
      </template>

      <template v-else>
        <hr class="my-2 border-blue-700">
        <a href="/profile" class="block px-6 py-3 text-lg font-medium text-white hover:bg-blue-700"
          @click="closeMobileMenu">个人中心</a>
        <a href="/account-settings" class="block px-6 py-3 text-lg font-medium text-white hover:bg-blue-700"
          @click="closeMobileMenu">账号设置</a>
        <button @click="logoutAndCloseMenu"
          class="w-full text-left px-6 py-3 text-lg font-medium text-red-300 hover:bg-blue-700">登出</button>
      </template>
    </nav>
  </header>
</template>

<script setup>
import { ref } from 'vue';

const isLoggedIn = ref(true);
const isMobileMenuOpen = ref(false);

const menuItems = [
  { name: '仪表盘', link: '/' },
  { name: '报告', link: '/reports' },
  { name: '数据源', link: '/data-sources' },
  { name: '设置', link: '/settings' }
];

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false;
};

const logout = () => {
  console.log('已登出');
  isLoggedIn.value = false;
  closeMobileMenu();
};

const logoutAndCloseMenu = () => {
  logout();
  closeMobileMenu();
}
</script>

<style scoped>
/* 让渐变背景动起来 (高级炫酷) */
header {
  background-size: 300% 300%;
  animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}
</style>
