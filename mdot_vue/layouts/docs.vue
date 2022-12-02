<template>
  <!-- docs.vue: this is the layout for documentation app -->
  <div :app-name="appName" :page-title="pageTitle">
    
    <header class="d-flex align-items-center h4 border-bottom bg-purple text-white">
      <div class="container">
      <a href="/vue" class="text-reset text-decoration-none">{{ appName }}</a>
      </div>
    </header>


    <main class="container">
      <h1 class="text-purple fw-bold">
        <slot name="title">
          {{ pageTitle }}
        </slot>
      </h1>

      <slot name="content" />
    </main>

    <footer class="text-white border-top bg-purple">
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
      appName: 'Mobile UW Developer Resources',
      // automatically set year
      currentYear: new Date().getFullYear(),
    };
  },
  created: function() {
    // constructs page title in the following format "Page Title - AppName"
    document.title = this.pageTitle + ' - ' + this.appName;
  },
};
</script>

<style lang="scss" scoped></style>
