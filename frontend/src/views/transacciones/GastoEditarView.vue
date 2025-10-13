<template>
    <RouterView/>
    <div class="row m-0">
        <!-- Botón de gasto -->
        <div class="col-6 d-flex justify-content-evenly">
            <button type="button" class="btn btn-success">Gasto</button>
        </div>
        <!-- Botón de ingreso -->
        <div class="col-6 d-flex justify-content-evenly">
            <button type="button" @click="router.push({ name: 'ingreso-editar' })"
                class="btn btn-outline-success">Ingreso</button>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router'


const router = useRouter()

</script>