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
          You have been designated as the sponsor for the app Test App. App
          Sponsors are responsible for adhering to the conditions set in the UW
          Terms and Conditions. Please fill out the app sponsor agreement form
          below to take responsibility for the app.
        </p>

        <p>
          Once the form is submitted, UW-IT will grant the App Manager Craig
          Stimmel developer access to the appropriate UW App Stores.
        </p>
      </div>
      <div class="row">
        <div class="col">
          <div class="row">
            <div class="col-8">
              <SponsorResposibilities></SponsorResposibilities>

              <hr class="my-4" />
              <DevResponsibilities></DevResponsibilities>

              <hr class="my-4" />
              <UWITResponsibilities></UWITResponsibilities>
            </div>
            <div class="col-4">
              <h3 class="h4 mb-3">App Details</h3>
              <ul class="list-group mb-4">
                <li class="list-group-item">
                  <div>
                    <h6 class="my-0">App Test</h6>
                    <small class="text-muted">App Name</small>
                  </div>
                </li>
                <li class="list-group-item">
                  <div>
                    <h6 class="my-0">Charlon Palacay</h6>
                    <small class="text-muted">App Sponsor</small>
                  </div>
                </li>
                <li class="list-group-item">
                  <div>
                    <h6 class="my-0">Craig Stimmel</h6>
                    <small class="text-muted">App Manager</small>
                  </div>
                </li>
                <li class="list-group-item">
                  <div>
                    <h6 class="my-0">ENG</h6>
                    <small class="text-muted">Primary Language</small>
                  </div>
                </li>
                <li class="list-group-item">
                  <div>
                    <h6 class="my-0">UW Apple Store</h6>
                    <small class="text-muted">Distribution Type</small>
                  </div>
                </li>
              </ul>

              <form class="border border-danger">
                <section class="sponsor-requirements">
                  <h3 class="h4 mb-3">Agreement</h3>
                  <p>
                    I certify that this form has been completed by the App
                    Sponsor listed above and that my answers are true and
                    complete to the best of my knowledge.
                  </p>

                  <div class="form-check">
                    <input
                      id="sponsor-requirements"
                      class="form-check-input"
                      name="sponsor-requirements"
                      required=""
                      type="checkbox"
                      checked
                    />
                    <label class="form-check-label" for="sponsor-requirements"
                      >I understand the Sponsor Responsibilities</label
                    >
                  </div>

                  <div class="form-check">
                    <input
                      id="understand-agreements"
                      class="form-check-input"
                      name="understand-agreements"
                      required=""
                      type="checkbox"
                      checked
                    />
                    <label class="form-check-label" for="understand-agreements"
                      >I understand the Services Offered by UW-IT</label
                    >
                  </div>

                  <div class="form-check">
                    <input
                      id="understand-manager"
                      class="form-check-input"
                      name="understand-manager"
                      required=""
                      type="checkbox"
                      checked
                    /><label class="form-check-label" for="understand-manager"
                      >I understand the App Manager Responsibilities</label
                    >
                  </div>
                </section>

                <div class="form-check mb-4">
                  <input
                    id="agree"
                    class="form-check-input"
                    name="agree"
                    required=""
                    type="checkbox"
                  />
                  <label class="form-check-label" for="agree"
                    >By clicking Accept, I have read and agree to the
                    responsibilities and conditions listed in this form.</label
                  >
                </div>

                <div class="row my-4">
                  <div class="col">
                    <input
                      class="w-100 mb-3 btn btn-purple btn-lg"
                      name="submit"
                      type="submit"
                      value="Accept"
                    />
                    <a
                      class="w-100 btn btn-outline-purple btn-lg"
                      href="/developers/decline/11"
                      >Decline</a
                    >
                  </div>
                </div>
              </form>
            </div>
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
      pageTitle: "Sponsor Agreement",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
