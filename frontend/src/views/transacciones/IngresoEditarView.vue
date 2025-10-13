<template>
    <RouterView/>
    <div class="row m-0">
        <!-- Botón de gasto -->
        <div class="col-6 d-flex justify-content-evenly">
            <button type="button" class="btn btn-outline-success"
                @click="router.push({ name: 'gasto-editar' })">Gasto</button>
        </div>
        <!-- Botón de ingreso -->
        <div class="col-6 d-flex justify-content-evenly">
            <button type="button" @click="router.push({ name: 'transaccion-crear-ingreso' })"
                class="btn btn-success">Ingreso</button>
        </div>
    </div>
</template>

<script setup>
import { RouterView, useRouter } from 'vue-router'

const router = useRouter()

</script>