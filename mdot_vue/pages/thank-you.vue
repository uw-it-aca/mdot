// about.vue

<template>
  <DocsLayout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <h3>Thank You</h3>
      <p>Your response has been recorded.</p>
      <p>
        The App Sponsor will be notified and asked to agree to the sponsor terms
        and conditions. Access to the Developer Program will be granted to the
        App Manager after the Sponsor submits the app sponsor agreement form.
      </p>
    </template>
  </DocsLayout>
</template>

<script>
import DocsLayout from "../layouts/docs.vue";

export default {
  components: {
    DocsLayout,
  },
  data() {
    return {
      pageTitle: "Thank You",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
