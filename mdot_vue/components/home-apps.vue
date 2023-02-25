<template>
  <div v-if="error">
    <p>Oops! Error encountered: {{ error.message }}</p>
  </div>
  <div v-else-if="data">
    <ul class="list-inline list-unstyled" style="--bs-columns: 3">
      <li
        v-for="app in data"
        :key="app.id"
        class="list-inline-item border rounded p-3"
        style="width: 200px"
      >
        <img
          v-if="app.image"
          :src="app.image"
          class="rounded-5"
          style="width: 200px"
        />
        <img v-else src="https://via.placeholder.com/100" class="rounded-5" />
        <p>{{ app.title }}</p>
        <p>{{ app.feature_desc }}</p>
        <ul>
          <li v-for="(resource, index) in app.resource_links" :key="index">
            {{ resource.link_type }}, {{ resource.url }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
  <div v-else>Loading...</div>
</template>

<script>
import { useFetch } from "../composables/fetch.js";
import mockData from "../../mdot/resources/mdot/file/api/v1/jsonmock/?featured=True";

export default {
  setup() {
    // if production... call api
    // useFetch and other composable methods can only be called from setup()
    if (process.env.NODE_ENV !== "localdev") {
      const baseUrl = "https://test-api.mdot.uw.edu/api/v1/uwresources/";
      const { data, error } = useFetch(baseUrl);
      return { data, error };
    }
  },

  created: function () {
    // if localdev... use mock data
    if (process.env.NODE_ENV == "localdev") {
      setTimeout(() => {
        this.loadStudent();
      }, 3000);
    }
  },
  data() {
    return {
      data: null,
      error: null,
    };
  },
  methods: {
    loadStudent: function () {
      console.log("hello world");
      this.error = "";
      this.data = mockData;
    },
  },
};
</script>
