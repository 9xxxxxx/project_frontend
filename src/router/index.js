import { createRouter, createWebHistory } from "vue-router";
import home from "@/views/home.vue";
import user from "@/views/user.vue";
import report from "@/views/report.vue";
import monitor from "@/views/monitor.vue";
import login from "@/views/login.vue";

const routes = [
  { path: "/home", component: home },
  { path: "/", component: home },
  { path: "/users", component: user },
  { path: "/reports", component: report },
  { path: "/monitor", component: monitor },
  { path: "/login", component: login },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
