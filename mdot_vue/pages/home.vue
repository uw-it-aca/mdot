// home.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque sed,
        officia adipisci, neque inventore nemo excepturi aspernatur rerum a
        totam aliquid in omnis quas, labore dolorum hic. Eligendi, vero aut.
      </p>

      <div class="mb-5">
        <HomeApps />
      </div>
      <p>
        <router-link :to="'/developers'"> developer resources</router-link>
      </p>
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
      pageTitle: "Welcome...",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
