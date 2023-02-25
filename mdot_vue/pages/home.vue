// home.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <HomeApps />
    </template>
  </layout>
</template>

<script>
import Layout from "../layouts/launcher.vue";
import HomeApps from "../components/home-apps.vue";

export default {
  components: {
    layout: Layout,
    HomeApps,
  },
  data() {
    return {
      pageTitle: "UW at your fingertips",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
