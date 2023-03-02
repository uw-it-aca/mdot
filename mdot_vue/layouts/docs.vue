<template>
  <!-- docs.vue: this is the layout for documentation app -->
  <div :app-name="appName" :page-title="pageTitle">
    <header
      class="d-flex align-items-center h4 border-bottom bg-purple text-white p-3"
    >
      <div class="container">
        <a href="/" class="text-reset text-decoration-none">{{ appName }}</a>
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
            <router-link :to="'/developers'">Developer Resources</router-link>
          </li>
          <li>
            <router-link :to="'/overview'"
              >Publishing Process Overview</router-link
            >
          </li>
          <li>
            <router-link :to="'/guidelines'">Publishing Guidelines</router-link>
          </li>
          <li>
            <router-link :to="'/access'">Request Access (vue form)</router-link>
          </li>
          <li>
            <router-link :to="'/agreement'"
              >Sponsor Agreement (vue form)</router-link
            >
          </li>
          <li>
            <router-link :to="'/agree'">Sponsor Agreed (vue form)</router-link>
          </li>
          <li>
            <router-link :to="'/decline'"
              >Sponsor Declined (vue form)</router-link
            >
          </li>
          <li>
            <a href="/request">Request Access (Django Sponsorship app OLD)</a>
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
