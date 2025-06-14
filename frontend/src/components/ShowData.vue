<template>
  <div v-if="loading">加载中...</div>
  <table v-else border="1" cellpadding="6">
    <thead>
      <tr>
        <th>日期</th>
        <th>合计工时</th>
        <th>责任部门</th>
        <th>作业描述</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="data in datas" :key="data.日期">
        <td>{{ data.日期 }}</td>
        <td>{{ data.合计工时 }}</td>
        <td>{{ data.责任部门 }}</td>
        <td>{{ data.作业描述 }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getMotorException } from '@/services/api'

const loading = ref(true)
const datas = ref([])

onMounted(async () => {
  try {
    const res = await getMotorException()
    datas.value = res.data
  } catch (err) {
    console.error('获取失败:', err)
  } finally {
    loading.value = false
  }
})
</script>