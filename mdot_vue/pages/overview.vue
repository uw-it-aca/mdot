// about.vue

<template>
  <DocsLayout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <h2 class="" id="page_header">
        What is the Mobile UW Developer Program?
      </h2>
      <p>
        the store is for anyone interested in publishing mobile apps through the
        Apple Developer and Google Play stores. Lorem ipsum dolor sit amet
        consectetur adipisicing elit. Ab aliquid voluptatum fugit, officiis
        quos, qui consectetur itaque incidunt a asperiores quidem, veritatis
        totam doloribus iste architecto cum eveniet. Impedit, harum. Grants
        access to the UW's Apple Developer Program. Android developers are good
        to go!
      </p>
      <div class="row mb-5">
        <div class="col">UW App Store (iOS)</div>
        <div class="col">UW Google Play Store (Android)</div>
      </div>

      <h2 class="" id="page_header">
        Mobile UW Developer Program
        <span class="nobreak">Publishing Process</span>
      </h2>
      <p class="">
        So, you have developed a native app and want to publish it under the UW
        Developer Store? Here is what you do next.
      </p>
      <ol class="list-unstyled">
        <li class="">
          <h3>Step 1</h3>
          Confirm that your app meets the requirements and responsibilities
          listed in the
          <a href="/guidelines" class="fw-bold"
            >Mobile UW Developer Program Publishing Guidelines</a
          >.
        </li>
        <li class="">
          <h3>Step 2</h3>
          Submit <a href="/access" class="fw-bold">your application</a> to
          request access to the <strong>Mobile UW Developer Program</strong>.
          <ul>
            <li>
              Designate an appropriate Sponsor who will be responsible for
              adhering to the conditions set in the UW App Developer Terms and
              Conditions.
            </li>
            <li>
              Designate an appropriate Developer (App Manager) who will be
              granted access.
            </li>
          </ul>
        </li>
        <li class="article">
          <h3>Step 3</h3>
          The designated Sponsor will receive an email asking them to agree to
          the Mobile UW Developer Program Agreement.
        </li>
        <li class="article">
          <h3>Step 4</h3>
          The Mobile UW Developer Program Team will process the request and
          grant the designated Developer access to the Mobile UW Developer
          Program.
        </li>
      </ol>
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
      pageTitle: "Program Overview",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
