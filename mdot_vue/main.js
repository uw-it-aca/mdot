import { createApp } from "vue";
import { createPinia } from "pinia";
// import VueGtag from "vue-gtag-next";
import { Vue3Mq, MqResponsive } from "vue3-mq";

// import axdd-components
import AxddComponents from "axdd-components";

import App from "./app.vue";
import router from "./router";

// bootstrap js + bootstrap-icons
import "bootstrap";
import "bootstrap-icons/font/bootstrap-icons.css";

// bootstrap (basic)
// import "./css/basic.scss";

// bootstrap (axdd) and axdd-components
import "./css/custom.scss";
// import "axdd-components/dist/style.css";

const app = createApp(App);
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
