<template>
  <!-- layout.vue: this is where you override the layout -->

  <div class="bg-purple text-white">
    <div class="container">
      <div class="row">
        <div class="col p-3">
          <header class="d-flex align-items-center pb-3 mb-5 h4">
            <a href="/" class="text-reset text-decoration-none">{{
              appName
            }}</a>
          </header>
          <h2 class="h5">Building a mobile app?</h2>
          <p class="text-white">
            Browse our curated
            <router-link :to="'/developers'"> developer resources</router-link>
            on building mobile websites and applications here at UW.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="row">
      <div class="col py-5" :app-name="appName" :page-title="pageTitle">
        <h1>
          <slot name="title">
            {{ pageTitle }}
          </slot>
        </h1>

        <slot name="content" />

        <footer class="pt-5 my-5 text-muted border-top">
          Copyright &copy; {{ currentYear }} University of Washington
        </footer>
      </div>
    </div>
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
