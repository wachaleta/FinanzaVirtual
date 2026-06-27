<template>
  <LoadingComponent/>
  <NavBar v-if="route.meta.useNavBar"/>
  <div class="px-3 pt-3">
    <RouterView/>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

import LoadingComponent from './components/LoadingComponent.vue';
import NavBar from './components/NavBar.vue';

const route = useRoute()

</script>

<style scoped>
/* .cargando {
    overflow: hidden;
    height: 100%;
} */
</style>