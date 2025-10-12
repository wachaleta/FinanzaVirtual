<template>
    <div class="row d-flex justify-content-evenly">
        <!-- Botón de gasto -->
        <div class="col-1">
            <button type="button" class="btn btn-outline-success"
                @click="router.push({ name: 'gasto-editar' })">Gasto</button>
        </div>
        <!-- Botón de ingreso -->
        <div class="col-1">
            <button type="button" @click="router.push({ name: 'transaccion-crear-ingreso' })"
                class="btn btn-success">Ingreso</button>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

</script>