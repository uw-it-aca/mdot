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
          Ready to submit your app for inclusion in the UW Development App
          Stores? Does it meet our
          <a href="/guidelines">publishing guidelines</a>?
        </p>
        <p class="article intro">
          If so, please fill out the form below. We will process your request
          and let you know the next steps.
        </p>
        <p>
          All the fields below must be filled out in order to submit this form.
        </p>
      </div>

      <div class="row">
        <div class="col-8">
          <form
            class="request-form"
            id="main-form"
            method="post"
            novalidate=""
            data-gtm-form-interact-id="0"
          >
            <input
              name="csrfmiddlewaretoken"
              type="hidden"
              value="3WS798EXYd3vmNZZVJF7DhbYVooeXM2tlOEj2mhwZUXMEKqh5horWd9x3qSTvjQo"
            />

            <h3 class="h4">App Information</h3>
            <p class="form-description">
              This portion of the form should be filled out with the details of
              the app you would like to submit to the UW App Store.
            </p>

            <div class="form-floating mb-3">
              <input
                id="id_app-name"
                class="form-control"
                maxlength="50"
                name="app-name"
                required=""
                placeholder="Application Name"
                type="text"
              />
              <label for="id_app-name">Application Name</label>
            </div>

            <div class="form-floating mb-3">
              <input
                id="id_app-primary_language"
                class="form-control"
                maxlength="20"
                name="app-primary_language"
                placeholder="e.g. English"
                required=""
                type="text"
              />
              <label for="id_app-primary_language">Primary language</label>
            </div>

            <hr class="my-4" />

            <p>Distribution Platform</p>
            <ul id="id_app-platform" class="list-unstyled">
              <li class="form-check">
                <input
                  id="id_app-platform_0"
                  class="form-check-input"
                  name="app-platform"
                  type="checkbox"
                  value="1"
                />
                <label class="form-check-label" for="id_app-platform_0"
                  >UW Google Play Store</label
                >
              </li>
              <li class="form-check">
                <input
                  id="id_app-platform_1"
                  class="form-check-input"
                  name="app-platform"
                  type="checkbox"
                  value="2"
                  data-gtm-form-interact-field-id="0"
                />

                <label class="form-check-label" for="id_app-platform_1"
                  >UW Apple Store</label
                >
              </li>
              <li class="form-check">
                <input
                  id="id_app-platform_2"
                  class="form-check-input"
                  name="app-platform"
                  type="checkbox"
                  value="3"
                />
                <label class="form-check-label" for="id_app-platform_2"
                  >Private Distribution</label
                >
              </li>
            </ul>

            <hr class="my-4" />

            <h3 class="form-heading">Developer Contact</h3>
            <p class="form-description">
              This portion of the form should be filled out with the details of
              the person who will be serving as the App Manager.
            </p>
            <p class="form-description">
              The App Manager will be responsible for code maintenance and app
              distribution.
            </p>

            <div class="row">
              <div class="col">
                <div class="form-floating mb-3">
                  <input
                    id="id_manager-first_name"
                    class="form-control"
                    maxlength="50"
                    name="manager-first_name"
                    required=""
                    type="text"
                    placeholder="First Name"
                  /><label for="id_manager-first_name">First name</label>
                </div>
              </div>
              <div class="col">
                <div class="form-floating mb-3">
                  <input
                    id="id_manager-last_name"
                    class="form-control"
                    maxlength="50"
                    name="manager-last_name"
                    required=""
                    type="text"
                    placeholder="Last Name"
                  /><label for="id_manager-last_name">Last name</label>
                </div>
              </div>
            </div>

            <div class="form-floating mb-3">
              <input
                id="id_manager-netid"
                class="form-control"
                maxlength="16"
                name="manager-netid"
                required=""
                type="text"
                placeholder="UW NetID"
              />
              <label for="id_manager-netid">UW NetID</label>
            </div>

            <div class="form-floating mb-3">
              <input
                id="id_manager-email"
                class="form-control"
                maxlength="256"
                name="manager-email"
                required=""
                type="email"
                placeholder="Email"
              />
              <label for="id_manager-email">Email</label>
            </div>

            <hr class="my-4" />

            <h3 class="form-heading">Sponsor Contact</h3>
            <p class="form-description">
              This portion of the form should be filled out with the details of
              the person who will be serving as the App Sponsor. The sponsor is
              a Director or above (or equivalent) at unit level within the
              University of Washington.
            </p>
            <p class="form-description">
              The App Sponsor will be notified and asked to agree to the sponsor
              terms and conditions.
            </p>

            <div class="row">
              <div class="col">
                <div class="form-floating mb-3">
                  <input
                    id="id_sponsor-first_name"
                    class="form-control"
                    maxlength="50"
                    name="sponsor-first_name"
                    required=""
                    type="text"
                    placeholder="xx"
                  />
                  <label for="id_sponsor-first_name">First name:</label>
                </div>
              </div>
              <div class="col">
                <div class="form-floating mb-3">
                  <input
                    id="id_sponsor-last_name"
                    class="form-control"
                    maxlength="50"
                    name="sponsor-last_name"
                    required=""
                    type="text"
                    placeholder="xx"
                  />
                  <label for="id_sponsor-last_name">Last name:</label>
                </div>
              </div>
            </div>

            <div class="form-floating mb-3">
              <input
                id="id_sponsor-netid"
                class="form-control"
                maxlength="16"
                name="sponsor-netid"
                required=""
                type="text"
                placeholder="xx"
              />
              <label for="id_sponsor-netid">UW NetID:</label>
            </div>

            <div class="form-floating mb-3">
              <input
                id="id_sponsor-email"
                class="form-control"
                maxlength="256"
                name="sponsor-email"
                required=""
                type="email"
                placeholder="xx"
              />
              <label for="id_sponsor-email">Email:</label>
            </div>

            <div class="form-floating mb-3">
              <input
                id="id_sponsor-title"
                class="form-control"
                maxlength="50"
                name="sponsor-title"
                required=""
                type="text"
                placeholder="xx"
              />
              <label for="id_sponsor-title">Title:</label>
            </div>

            <div class="row">
              <div class="col">
                <div class="form-floating mb-3">
                  <input
                    id="id_sponsor-department"
                    class="form-control"
                    maxlength="30"
                    name="sponsor-department"
                    required=""
                    type="text"
                    placeholder="xx"
                  />
                  <label for="id_sponsor-department">Department:</label>
                </div>
              </div>
              <div class="col">
                <div class="form-floating mb-3">
                  <input
                    id="id_sponsor-unit"
                    class="form-control"
                    maxlength="30"
                    name="sponsor-unit"
                    required=""
                    type="text"
                    placeholder="xx"
                  />
                  <label for="id_sponsor-unit">Unit:</label>
                </div>
              </div>
            </div>

            <hr class="my-4" />
            <div class="text-end my-5">
              <button class="w-100 btn btn-purple btn-lg" type="submit">
                Request Access
              </button>
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
      pageTitle: "Request Access",
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
