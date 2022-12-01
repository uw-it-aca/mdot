import { createWebHistory, createRouter } from "vue-router";
import { trackRouter } from "vue-gtag-next";

// page components
import Home from '../pages/home.vue';
import Resources from '../pages/resources.vue';

const routes = [
  {
    path: "/vue",
    component: Home
  },
  {
    path: "/vue/resources",
    component: Resources,
    pathToRegexpOptions: { strict: true }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// vue-gtag-next router tracking
trackRouter(router);

export default router;
