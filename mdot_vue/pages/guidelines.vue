// about.vue

<template>
  <DocsLayout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <div class="py-5">
        <p class="lead">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis totam
          assumenda commodi natus sed magnam, ullam fugiat vitae perferendis
          maxime vel dolor adipisci non at quisquam ut dolores neque voluptatum.
        </p>
      </div>
      <div class="row">
        <div class="col-8">
          <h2 class="mb-3 text-purple">Requirements</h2>
          <p>
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ut laborum
            suscipit eos minus, sint doloremque necessitatibus reiciendis
            fugiat. Ut itaque illum distinctio vel natus at animi architecto
            tenetur perspiciatis rem?
          </p>
          <ul class="list-unstyled">
            <li class="mb-4">
              <h3 class="h4 mb-3">Meet campus needs</h3>
              The app must meet known needs of broad campus-wide audiences. If
              it is intended for very specific audiences (such as a class,
              department, or school), we advise departments and schools to set
              up their own App Stores. If you need assistance in doing this,
              please feel free to contact us at EMAIL ADDRESS.
            </li>
            <li class="mb-4">
              <h3 class="h4 mb-3">Sponsorship &amp; support</h3>
              <p>The app must have a clearly identified:</p>
              <ul>
                <li>
                  Official sponsor affiliated with the UW (UWNetID, contact
                  info)
                </li>
                <li>
                  Maintainer/publisher (single contact) (name, contact info)
                </li>
                <li>Support Channel (contact info)</li>
              </ul>
            </li>
          </ul>

          <hr />

          <h2 class="mb-3 text-purple">Responsibilities</h2>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam
            deleniti voluptatum libero iure temporibus reprehenderit soluta
            officia repellat explicabo a dolorem ducimus recusandae sint hic
            sit, praesentium minus eaque minima.
          </p>
          <ul class="list-unstyled">
            <li class="mb-4">
              <SponsorResposibilities></SponsorResposibilities>
            </li>
            <li class="mb-4">
              <DevResponsibilities></DevResponsibilities>
            </li>
            <li class="mb-4">
              <UWITResponsibilities></UWITResponsibilities>
            </li>
          </ul>
        </div>
        <div class="col-4">
          <div>
            <h3 class="h4 mb-3">Request Access</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae
              corporis quos perspiciatis earum eius quisquam culpa aliquid,
              doloremque ducimus repellendus minima tempore, nihil recusandae,
              voluptas a iure quam! A, beatae.
            </p>

            <p><a href="/access">Request access</a></p>
          </div>
          <div>
            <h3 class="h4 mb-3">Developer Resources</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae
              corporis quos perspiciatis earum eius quisquam culpa aliquid,
              doloremque ducimus repellendus minima tempore, nihil recusandae,
              voluptas a iure quam! A, beatae.
            </p>
            <p>
              Still need help? Refer to our
              <a href="/developers">developer resources</a> for more
              information.
            </p>
          </div>
        </div>
      </div>
    </template>
  </DocsLayout>
</template>

<script>
import DocsLayout from "../layouts/docs.vue";
import SponsorResposibilities from "../components/SponsorResposibilities.vue";
import DevResponsibilities from "../components/DevResponsibilities.vue";
import UWITResponsibilities from "../components/UWITResponsibilities.vue";

export default {
  components: {
    DocsLayout,
    SponsorResposibilities,
    DevResponsibilities,
    UWITResponsibilities,
  },
  data() {
    return {
      pageTitle: "Publishing Guidelines",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
