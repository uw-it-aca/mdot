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
          <form>
            <div class="row">
              <div class="col-8">
                <input
                  name="csrfmiddlewaretoken"
                  type="hidden"
                  value="v3AVpmRF9ayyeNqiycgjMB2wRIwCZvjjNVm7iAueaRsPwKRAIKZD5x05ZK0hx27e"
                />

                <section class="sponsor-requirements">
                  <h3 class="h4">Sponsor Responsibilities</h3>
                  <ul>
                    <li>
                      <strong>UW Terms and Conditions</strong>
                      <p>
                        You will be responsible for adhering to the conditions
                        set out in the UW
                        <a href="https://www.washington.edu/online/terms/"
                          >Terms and Conditions.</a
                        >
                      </p>
                    </li>
                    <li>
                      <strong
                        >Apple and/or Google Play Terms and Conditions</strong
                      >
                      <p>
                        You will be responsible for adhering to the conditions
                        set out in the
                        <a href="https://developer.apple.com/terms/">Apple</a>
                        and/or
                        <a
                          href="https://play.google.com/about/play-terms/index.html"
                          >Google Play</a
                        >
                        terms and conditions.
                      </p>
                    </li>
                    <li>
                      <strong>Usability (User Experience)</strong>
                      <p>
                        The UW is committed to providing good user experience
                        for our audiences. For assistance, free
                        <a
                          href="https://uw.service-now.com/uwc.do?sysparm_direct=true#/catalog_order/3494e9951385a3c0c20bb9004244b073"
                          >UX consultations</a
                        >
                        are available with UW-IT's AXDD design team.
                      </p>
                    </li>
                    <li>
                      <strong>Accessibility</strong>
                      <p>
                        It is UW policy that all software is
                        <a
                          href="https://www.washington.edu/accessibility/guidelines/"
                          >accessible</a
                        >. For assistance, UW-IT's Accessible Technology
                        Services (ATS) team offers
                        <a href="https://www.washington.edu/accessibility/help/"
                          >accessiblity consultations/reviews</a
                        >.
                      </p>
                    </li>
                    <li>
                      <strong>UW Privacy Statement</strong>
                      <p>
                        You will be responsible for adhering to the UW
                        <a href="https://www.washington.edu/online/privacy/"
                          >Online Privacy Statement</a
                        >.
                      </p>
                    </li>
                    <li>
                      <strong>UW Branding</strong>
                      <p>
                        If applicable, adhere to the use of UW
                        <a href="http://www.washington.edu/brand/"
                          >logo and brand guidelines</a
                        >.
                      </p>
                    </li>
                    <li>
                      <strong>Due Diligence</strong>
                      <p>
                        You agree to undertake the due diligence to adhere to
                        the UW values and demonstrate compliance with all UW
                        policies mentioned and/or may otherwise be relevant.
                      </p>
                    </li>
                  </ul>
                  <label for="sponsor-requirements"
                    ><input
                      id="sponsor-requirements"
                      name="sponsor-requirements"
                      required=""
                      type="checkbox"
                    />I agree to the App Sponsor responsibilities</label
                  >
                </section>
                <hr />
                <section class="sponsor-requirements">
                  <h3 class="h4">Services Offered by UW-IT</h3>
                  <ul>
                    <li>
                      <strong
                        >Application ID Creation and App Manager
                        Provisioning</strong
                      >
                      <p>
                        UW-IT shall create a single application ID and assign an
                        App Manager (specified above).
                      </p>
                    </li>
                    <li>
                      <strong>Audit</strong>
                      <p>
                        UW-IT may perform audits to ensure that accounts are up
                        to date and applications are in good standing. We are
                        also responsible to audit any apps if we have received
                        any formal complaints and/or requests from Apple/Google.
                      </p>
                    </li>
                    <li>
                      <strong>App Suspension and/or Removal</strong>
                      <p>
                        UW-IT reserves the right to suspend or remove apps in
                        the store that violate any of the terms and conditions
                        described above.
                      </p>
                    </li>
                    <li>
                      <strong>Support</strong>
                      <p>
                        UW-IT provides minimal technical support in the form of
                        technical advice/guidance and knowledge expertise. No
                        support provided for application development.
                      </p>
                    </li>
                  </ul>
                  <label for="understand-agreements"
                    ><input
                      id="understand-agreements"
                      name="understand-agreements"
                      required=""
                      type="checkbox"
                    />I understand the services offered by UW-IT</label
                  >
                </section>
                <hr />
                <section class="sponsor-requirements">
                  <h3>App Manager Responsibilities</h3>
                  <ul>
                    <li>
                      <strong>Developer Account Invitations</strong>
                      <p>
                        The App Manager is responsible for inviting users to
                        their specific application team as well as maintaining
                        their team in good standing - removing members who are
                        no longer part of their team. AXDD reserves the right to
                        remove or update membership for members not added to a
                        specific application team or that are no longer actively
                        participating in development.
                      </p>
                    </li>
                    <li>
                      <strong>Publishing Application</strong>
                      <p>
                        The App Manager is responsible for overall publishing of
                        the app.
                      </p>
                    </li>
                  </ul>
                  <label for="understand-manager"
                    ><input
                      id="understand-manager"
                      name="understand-manager"
                      required=""
                      type="checkbox"
                    />I understand the App Manager responsibilities</label
                  >
                </section>
                <hr />
                <section class="sponsor-requirements">
                  <h3>Agreement</h3>
                  <p>
                    I certify that this form has been completed by the App
                    Sponsor listed above and that my answers are true and
                    complete to the best of my knowledge.
                  </p>
                  <label for="agree"
                    ><input
                      id="agree"
                      name="agree"
                      required=""
                      type="checkbox"
                    />I agree to the policies and conditions listed in this
                    form.</label
                  >
                </section>

                <hr class="my-4" />

                <div class="row mb-5">
                  <div class="col">
                    <input
                      class="w-100 btn btn-purple btn-lg"
                      name="submit"
                      type="submit"
                      value="Agree and Accept"
                    />
                  </div>
                  <div class="col">
                    <a
                      class="w-100 btn btn-outline-purple btn-lg"
                      href="/developers/decline/11"
                      >Decline</a
                    >
                  </div>
                </div>
              </div>
              <div class="col-4">
                <h3 class="h4">App Details</h3>
                <ul class="list-group">
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
              </div>
            </div>
          </form>
        </div>
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
      pageTitle: "Sponsor Agreement",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
