<template>
  <!-- docs.vue: this is the layout for documentation app -->
  <div :app-name="appName" :page-title="pageTitle">
    <header class="h4 border-bottom bg-purple text-white py-3">
      <div class="container">
        <div class="row">
          <div class="col">
            <a href="/" class="text-reset text-decoration-none">{{
              appName
            }}</a>
          </div>
        </div>
      </div>
    </header>

    <main class="container">
      <h1 class="text-purple fw-bold">
        <slot name="title">
          {{ pageTitle }}
        </slot>
      </h1>

      <nav>
        <ul>
          <li>
            <a href="/developers">Developer Resources</a>
          </li>
          <li>
            <a href="/overview">Program Overview</a>
          </li>
          <li>
            <a href="/guidelines">Publishing Guidelines</a>
          </li>

          <li>
            <a href="/request">Request Access (Vue compiled on request.html)</a>
            <ul>
              <li>
                <a href="/agreement">Sponsor Agreement (vue form)</a>
              </li>
              <li>
                <a href="/agree">Sponsor Agreed (vue get)</a>
              </li>
              <li>
                <a href="/decline">Sponsor Declined (vue get)</a>
              </li>
              <li>
                <a href="/thank-you">Sponsor Thank You (vue)</a>
              </li>
            </ul>
          </li>
        </ul>
      </nav>
      <slot name="content" />
    </main>

    <footer class="border-top bg-purple text-white p-3">
      <div class="container">
        Copyright &copy; {{ currentYear }} University of Washington
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  components: {},
  props: {
    pageTitle: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      // minimum application setup overrides
      appName: "Mobile UW",
      // automatically set year
      currentYear: new Date().getFullYear(),
    };
  },
  created: function () {
    // constructs page title in the following format "Page Title - AppName"
    document.title = this.pageTitle + " - " + this.appName;
  },
};
</script>

<style lang="scss" scoped></style>
