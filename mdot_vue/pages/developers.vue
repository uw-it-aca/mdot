// about.vue

<template>
  <layout :page-title="pageTitle">
    
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #content>
      <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolores fuga eius, amet maxime odit mollitia, ducimus voluptas ullam unde obcaecati voluptatibus laborum ea quod perferendis nobis, nemo officiis? Sint, dolore.</p>
    </template>
  </layout>
</template>

<script>
import { Card } from 'axdd-components';
import Layout from '../layout.vue';
import HelloWorld from '../components/hello-world.vue';

export default {
  components: {
    layout: Layout,
    'hello-world': HelloWorld,
    'axdd-card': Card,
  },
  data() {
    return {
      pageTitle: 'Developers',
    };
  },
  methods: {},
};
</script>

<style lang="scss"></style>
