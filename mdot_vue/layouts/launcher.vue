<template>
  <!-- layout.vue: this is where you override the layout -->
  <div
    class="col-lg-8 mx-auto p-3 py-md-5"
    :app-name="appName"
    :page-title="pageTitle"
  >
    <header class="d-flex align-items-center pb-3 mb-5 h4 border-bottom">
      <a href="/" class="text-reset text-decoration-none">{{ appName }}</a>
    </header>

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
