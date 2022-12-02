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
      <p><a href="/vue/resources">Go to mobile development resources</a></p>
    </template>
  </layout>
</template>

<script>
import Layout from "../layouts/launcher.vue";

export default {
  components: {
    layout: Layout,
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
