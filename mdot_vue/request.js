import { createApp } from "vue";
import RequestApp from "./RequestApp.vue";

// import VueGtag from "vue-gtag-next";
import { Vue3Mq, MqResponsive } from "vue3-mq";

// import axdd-components
import AxddComponents from "axdd-components";

// bootstrap js + bootstrap-icons
import "bootstrap";
import "bootstrap-icons/font/bootstrap-icons.css";

// bootstrap (basic)
// import "./css/basic.scss";

// bootstrap (axdd) and axdd-components
import "./css/custom.scss";
// import "axdd-components/dist/style.css";


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

// axdd-components
app.use(AxddComponents);


createApp(RequestApp).mount("#request");