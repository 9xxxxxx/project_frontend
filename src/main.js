import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import naive from 'naive-ui'


// createApp(App).mount('#app')
const app = createApp(App)
app.use(router)
app.use(naive)
app.mount('#app')
// createApp(App).use(router).mount('#app')