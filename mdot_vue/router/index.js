import { createWebHistory, createRouter } from "vue-router";

// vue-gtag-next track routing
// import { trackRouter } from "vue-gtag-next";

// page components
import LauncherApp from "../pages/home.vue";
import DevResources from "../pages/developers.vue";
import PubGuidelines from "../pages/guidelines.vue";
import ProcessOverview from "../pages/process.vue";

const routes = [
  {
    path: "/vue",
    component: LauncherApp,
  },
  {
    path: "/developers",
    component: DevResources,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/guidelines",
    component: PubGuidelines,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/process",
    component: ProcessOverview,
    pathToRegexpOptions: { strict: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// vue-gtag-next router tracking
// trackRouter(router);

export default router;
