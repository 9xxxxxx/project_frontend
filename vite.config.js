import { fileURLToPath, URL } from 'node:url'
import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  // 加载环境变量（支持 .env 文件）
  const env = loadEnv(mode, process.cwd(), ['VITE_'])
  
  return {
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      },
    },
    plugins: [vue(), vueDevTools(), tailwindcss()],
    server: {
      host: '0.0.0.0',
      port: 17608,
      proxy: {
        '/api': env.VITE_API_BASE_URL || 'http://localhost:8000'
      }
    },
    define: {
      // 将环境变量注入到前端代码
      'import.meta.env.VITE_API_BASE_URL': JSON.stringify(env.VITE_API_BASE_URL)
    }
  }
})
