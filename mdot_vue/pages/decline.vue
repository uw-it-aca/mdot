// about.vue

<template>
  <DocsLayout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <div class="container">
        <h2 class="mdot-subhead" id="page_header">Review App Request</h2>

        <h3>Thank You</h3>
        <p>
          You have declined the role of App Sponsor for <strong>xxxxx</strong>.
        </p>
        <p>
          The designated App Manager will not be granted access to the Developer
          Program under your sponsorship.
        </p>
      </div>
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
      pageTitle: "Declined",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
