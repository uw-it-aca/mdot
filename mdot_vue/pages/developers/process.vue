// about.vue

<template>
  <DocsLayout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <h2 class="mdot-subhead" id="page_header">
        UW Developer Store <span class="nobreak">Publishing Process</span>
      </h2>
      <p class="article intro">
        So, you have developed a native app and want to publish it under the UW
        Developer Store? Here is what you do next.
      </p>
      <ol class="trad-list process-page">
        <li class="article">
          <h3>Step 1</h3>
          Confirm that your app meets the
          <a href="/developers/guidelines"
            >UW Developer Store Publishing Guidelines</a
          >.
        </li>
        <li class="article">
          <h3>Step 2</h3>
          Submit <a href="/developers/request">your application</a> to request
          access to the UW Developer Store.
          <ul>
            <li>
              Designate an appropriate App Manager who will be granted access to
              the UW Developer Program.
            </li>
            <li>
              Designate an appropriate App Sponsor who will be responsible for
              adhering to the conditions set in the UW App Developer Terms and
              Conditions.
            </li>
          </ul>
        </li>
        <li class="article">
          <h3>Step 3</h3>
          The designated App Sponsor will receive an email asking them to agree
          to the UW App Developer Terms and Conditions.
        </li>
        <li class="article">
          <h3>Step 4</h3>
          The UW-IT Mobile Team will process the request and grant the
          designated App Manager access to the UW Developer Program.
        </li>
      </ol>
    </template>
  </DocsLayout>
</template>

<script>
import DocsLayout from "../../layouts/developers.vue";

export default {
  components: {
    DocsLayout,
  },
  data() {
    return {
      pageTitle: "Process Overview",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
