import { createRouter, createWebHistory } from "vue-router";
import home from "@/pages/home.vue";

const routes = [
  { path: "/home", component: home },
  { path: "/", component: home },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
