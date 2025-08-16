<template>
  <NavBar/>
  <div class="px-3">
    <router-view/>
  </div>
</template>

<script setup>
import NavBar from './components/NavBar.vue';
</script>

<style scoped>
</style>