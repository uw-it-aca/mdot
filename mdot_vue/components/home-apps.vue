<template>
  <div v-if="error">
    <p>Oops! Error encountered: {{ error.message }}</p>
  </div>
  <div v-else-if="data">
    <ul class="list-inline list-unstyled row">
      <li
        v-for="app in data"
        :key="app.id"
        class="list-inline-item p-3 col-4 col-sm-3 col-lg-2 m-0"
      >
        <template v-for="(resource, index) in app.resource_links" :key="index">
          <div v-if="resource.link_type == 'WEB'">
            <a :href="resource.url">
              <div
                v-if="app.image"
                class="square border rounded-4"
                :style="'background-image: url(' + app.image + ')'"
              ></div>

              <div
                v-else
                class="square border rounded-4"
                style="background-image: url('https://via.placeholder.com/190')"
              ></div>
            </a>
          </div>
        </template>

        <p class="text-center text-uppercase mt-3 fs-5 fw-light">{{ app.title }}</p>
        <p>{{ app.feature_desc }}</p>

        <div>
          <template
            v-for="(resource, index) in app.resource_links"
            :key="index"
          >
            <span v-if="resource.link_type == 'AND'" class="me-2 text-nowrap">
              <a :href="resource.url"><i class="bi bi-android2"></i>AND</a>
            </span>
            <span v-if="resource.link_type == 'IOS'" class="me-2 text-nowrap">
              <a :href="resource.url"><i class="bi bi-apple"></i>iOS</a>
            </span>
          </template>
        </div>
      </li>
    </ul>
  </div>
  <div v-else>Loading...</div>
</template>

<script>
import { useFetch } from "../composables/fetch.js";
import mockData from "../../mdot/resources/mdot/file/api/v1/jsonmock/";
import { link } from "fs/promises";

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

<style lang="scss">
.square {
  width: 100%;
  padding-bottom: 100%;
  background-size: cover;
  background-position: center;
  transition-duration: 0.2s;
  transition-property: transform;
}

.square:hover {
  transform: scale(1.05);
}
</style>
