// about.vue

<template>
  <DocsLayout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <h2>
        UW Developer Store <span class="nobreak">Publishing Guidelines</span>
      </h2>

      <ol>
        <li class="article">
          <h3>Meet campus needs</h3>
          The app must meet known needs of broad campus-wide audiences. If it is
          intended for very specific audiences (such as a class, department, or
          school), we advise departments and schools to set up their own App
          Stores. If you need assistance in doing this, please feel free to
          contact us at
          <a href="mailto:{{ service_email }}">{{ service_email }}</a
          >.
        </li>
        <li class="article">
          <h3>Sponsorship &amp; support</h3>
          The app must have a clearly identified:
          <ul>
            <li>
              Official sponsor affiliated with the UW (UWNetID, contact info)
            </li>
            <li>Maintainer/publisher (single contact) (name, contact info)</li>
            <li>Support Channel (contact info)</li>
          </ul>
        </li>
        <li>
          <h3>Sponsor responsibilities</h3>
          <section class="sponsor-requirements">
            <ul>
              <li>
                <strong>UW Terms and Conditions</strong>
                <p>
                  You will be responsible for adhering to the conditions set out
                  in the UW
                  <a href="https://www.washington.edu/online/terms/"
                    >Terms and Conditions.</a
                  >
                </p>
              </li>
              <li>
                <strong>Apple and/or Google Play Terms and Conditions</strong>
                <p>
                  You will be responsible for adhering to the conditions set out
                  in the
                  <a href="https://developer.apple.com/terms/">Apple</a> and/or
                  <a href="https://play.google.com/about/play-terms/index.html"
                    >Google Play</a
                  >
                  terms and conditions.
                </p>
              </li>
              <li>
                <strong>Usability (User Experience)</strong>
                <p>
                  The UW is committed to providing good user experience for our
                  audiences. For assistance, free
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
                  <a href="https://www.washington.edu/accessibility/guidelines/"
                    >accessible</a
                  >. For assistance, UW-IT's Accessible Technology Services
                  (ATS) team offers
                  <a href="https://www.washington.edu/accessibility/help/"
                    >accessiblity consultations/reviews</a
                  >.
                </p>
              </li>
              <li class="text-danger">
                <strong>External Vendors/Developers</strong>
                <p>
                  If you are working with an external vendor or developer, you will be responsible for ensuring the vendor/developer is in compliance with UW policies regarding data security and privacy and that any necessary agreements to that regard are in place. The Office of the CISO or Procurement Services may be able to provide guidance.
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
                  You agree to undertake the due diligence to adhere to the UW
                  values and demonstrate compliance with all UW policies
                  mentioned and/or may otherwise be relevant.
                </p>
              </li>
            </ul>
          </section>
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
      pageTitle: "Guidelines",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
