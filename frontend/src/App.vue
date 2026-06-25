<template>
  <LoadingComponent/>
  <NavBar/>
  <div class="px-3 pt-3">
    <RouterView/>
  </div>
</template>

<script setup>
import LoadingComponent from './components/LoadingComponent.vue';
import NavBar from './components/NavBar.vue';
</script>

<style scoped>
/* .cargando {
    overflow: hidden;
    height: 100%;
} */
</style>