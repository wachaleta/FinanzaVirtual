<style>
/* Contenedor de la pantalla de carga */
.loader-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(172, 172, 172, 0.9); /* Fondo semitransparente */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 9999; /* Asegura que esté por encima de todo */
}

/* Animación del spinner */
.spinner {
    width: 50px;
    height: 50px;
    border: 5px solid #dedede;
    border-top: 5px solid #5cb4ee;
    border-radius: 50%;
    animation: girar 1s linear infinite;
}

@keyframes girar {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>

<template>
    <div v-if="loading.show" class="loader-container">
        <div class="spinner"></div>
        <p>Cargando...</p>
    </div>
</template>

<script setup>

import { useLoadingStore } from '@/store/useLoadingStore'

const loading = useLoadingStore();

</script>