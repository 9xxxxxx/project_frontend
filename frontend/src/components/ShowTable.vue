<script setup>
import { ref, onMounted } from "vue";
import * as echarts from "echarts";
import axios from "axios";
import { API_BASE_URL } from "@/config";
import { defineComponent } from 'vue'
import { NButton } from 'naive-ui'

const chartRef = ref(null);

onMounted(async () => {
  const res = await axios.get(`${API_BASE_URL}/api/getdata/`);
  const rawData = res.data;

  // 聚合数据（按日期合并）
  const aggregated = {};
  rawData.forEach((item) => {
    const date = item["日期"];
    if (!aggregated[date]) {
      aggregated[date] = {
        man: 0,
        hours: 0,
        output: 0,
      };
    }
    aggregated[date].man += item["标准人力"];
    aggregated[date].hours += item["标准工时"];
    aggregated[date].output += item["标准产量"];
  });
  
  // 整理成图表需要的数据结构
  const date = Object.keys(aggregated).sort();
  const man = date.map((d) => aggregated[d].man);
  const hours = date.map((d) => aggregated[d].hours);
  const output = date.map((d) => aggregated[d].output);

  const chart = echarts.init(chartRef.value);
  chart.setOption({
    title: { text: "电机 KPI 走势" },
    tooltip: { trigger: "axis" },
    xAxis: { type: "category", data: date },
    yAxis: { type: "value", name: "数量" },
    legend: {
      data: ["人力", "工时", "产量"],
      right: "120px",
    },
    series: [
      {
        name: "人力",
        type: "line",
        data: man,
        lineStyle: { color: "#5470C6" },
        label: { show: true },
      },
      {
        name: "工时",
        type: "line",
        data: hours,
        lineStyle: { color: "#91CC75" },
        label: { show: true },
      },
      {
        name: "产量",
        type: "line",
        data: output,
        lineStyle: { color: "#EE6666" },
        label: { show: true },
      },
    ],
  });
});
</script>


<template>
  <div>
    <div ref="chartRef" class="chart"></div>
     <n-button class="w-full bg-blue-500 text-white py-2 rounded-md shadow-md hover:bg-blue-600 transition duration-200">naive-ui</n-button>
  </div>
</template>



<style scoped>
.chart{
    width: 1200px;
    height: 500px;
}
</style>