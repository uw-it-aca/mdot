<template>
  <div v-if="error">
    <p>Oops! Error encountered: {{ error.message }}</p>
  </div>
  <div v-else-if="data">
    Data loaded:
    <pre>{{ data }}</pre>
  </div>
  <div v-else>Loading...</div>

  <ul class="list-inline">
    <li v-for="app in apps" :key="app.id" class="list-inline-item">
      <img v-if="app.image" :src="app.image" class="img-thumbnail" style="width:200px;" />
      <img v-else src="https://via.placeholder.com/200" />
      <p>{{ app.title }}</p>
    </li>
  </ul>
</template>

<script>
import { useFetch } from "../composables/fetch.js";
import appsData from "../resources/apps.json";

export default {
  setup() {
    const baseUrl = "https://test-api.mdot.uw.edu/api/v1/uwresources/";
    const { data, error } = useFetch(baseUrl);
    return { data, error };
  },
  data() {
    return {
      apps: appsData,
    };
  },
};
</script>
