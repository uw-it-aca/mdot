import { createWebHistory, createRouter } from "vue-router";

// vue-gtag-next track routing
// import { trackRouter } from "vue-gtag-next";

// page components
import LauncherApp from "../pages/launcher.vue";
import DevIndex from "../pages/developers/index.vue";
import DevGuidelines from "../pages/developers/guidelines.vue";
import DevProcess from "../pages/developers/process.vue";

const routes = [
  {
    path: "/",
    component: LauncherApp,
  },
  {
    path: "/developers",
    component: DevIndex,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/developers/guidelines",
    component: DevGuidelines,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/developers/process",
    component: DevProcess,
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
