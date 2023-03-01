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
          Your acceptance of the App Sponsor position for
          <strong>xxxxx</strong> has been recorded.
        </p>
        <p>
          UW-IT will grant developer access to the designated App Manager under
          your sponsorship.
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
      pageTitle: "Agreed",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
