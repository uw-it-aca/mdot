<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <HomeList />
    </template>
  </layout>
</template>

<script>
import Layout from "../layouts/launcher.vue";
import HomeList from "../components/HomeList.vue";

export default {
  components: {
    layout: Layout,
    HomeList,
  },
  data() {
    return {
      pageTitle: "UW at your fingertips",
    };
  },
  methods: {},
};
</script>
