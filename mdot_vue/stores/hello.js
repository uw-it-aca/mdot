import { defineStore } from "pinia";

export const useHelloStore = defineStore({
  // id is required so that Pinia can connect the store to the devtools
  id: "hello",
  state: () => ({ message: "Hello world, from Pinia" }),
  getters: {},
  actions: {},
});
