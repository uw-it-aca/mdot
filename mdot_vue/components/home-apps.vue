<template>
  <div v-if="error">
    <p>Oops! Error encountered: {{ error.message }}</p>
  </div>
  <div v-else-if="data">
    Data loaded:
    <pre>{{ data }}</pre>
  </div>
  <div v-else>Loading...</div>
</template>

<script>
import { useFetch } from "../composables/fetch.js";

export default {
  setup() {
    const baseUrl = "https://test-api.mdot.uw.edu/api/v1/uwresources/";
    const { data, error } = useFetch(baseUrl);
    return { data, error };
  },
};
</script>
