// about.vue

<template>
  <layout :page-title="pageTitle">
    
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <h2>Things to Consider</h2>
      
      <h3>Mobile Web vs. Native vs. Hybrid</h3>
      <p>Before deciding what to build, understand your options. Mobile web is the most versatile and easiest to maintain, but can be limiting if you need robust device integration.</p>
    
    </template>
  </layout>
</template>

<script>
import Layout from '../components/layouts/docs.vue';

export default {
  components: {
    layout: Layout,
  },
  data() {
    return {
      pageTitle: 'Resources',
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
