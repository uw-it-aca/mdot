import { createApp } from "vue";
import { createPinia } from "pinia";
// import VueGtag from "vue-gtag-next";
import { Vue3Mq, MqResponsive } from "vue3-mq";
import { createWebHistory, createRouter } from "vue-router";

// page components
import LauncherApp from "./pages/home.vue";
import DevResources from "./pages/developers.vue";
import PubGuidelines from "./pages/guidelines.vue";
import ProcessOverview from "./pages/overview.vue";
import SponsorAgreement from "./pages/agreement.vue";
import SponsorAgree from "./pages/agree.vue";
import SponsorDecline from "./pages/decline.vue";
import ThankYou from "./pages/thank-you.vue";

const routes = [
  {
    path: "/",
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
    path: "/overview",
    component: ProcessOverview,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/agreement",
    component: SponsorAgreement,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/agree",
    component: SponsorAgree,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/decline",
    component: SponsorDecline,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/thank-you",
    component: ThankYou,
    pathToRegexpOptions: { strict: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// import axdd-components
import AxddComponents from "axdd-components";

import MainApp from "./main-app.vue";

// bootstrap js + bootstrap-icons
import "bootstrap";
import "bootstrap-icons/font/bootstrap-icons.css";

// bootstrap (basic)
// import "./css/basic.scss";

// bootstrap (axdd) and axdd-components
import "./css/custom.scss";
// import "axdd-components/dist/style.css";

const app = createApp(MainApp);
app.config.productionTip = false;

// vue-gtag-next
// TODO: un-commment to use Google Analytics for you app. also
// configure trackRouter located in the router/index.js file

/*
const gaCode = document.body.getAttribute("data-google-analytics");
const debugMode = document.body.getAttribute("data-django-debug");

app.use(VueGtag, {
  isEnabled: debugMode == "false",
  property: {
    id: gaCode,
    params: {
      anonymize_ip: true,
      // user_id: 'provideSomeHashedId'
    },
  },
});
*/

// vue-mq (media queries)
app.use(Vue3Mq, {
  preset: "bootstrap5",
});
app.component("mq-responsive", MqResponsive);

// pinia (vuex) state management
const pinia = createPinia();
app.use(pinia);

// axdd-components
app.use(AxddComponents);

// vue-router
app.use(router);

app.mount("#app");
