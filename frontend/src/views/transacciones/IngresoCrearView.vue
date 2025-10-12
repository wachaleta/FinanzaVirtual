<template>
    <!-- Botones de selección de transacción -->
    <div class="row d-flex justify-content-evenly">
        <!-- Botón de gasto -->
        <div class="col-1">
            <button type="button" class="btn btn-outline-success"
                @click="router.push({ name: 'transaccion-crear-gasto' })">Gasto</button>
        </div>
        <!-- Botón de ingreso -->
        <div class="col-1">
            <button type="button" @click="router.push({ name: 'transaccion-crear-ingreso' })"
                class="btn btn-success">Ingreso</button>
        </div>
        <!-- Botón de transferencia -->
        <div class="col-1">
            <button type="button" @click="router.push({ name: 'transaccion-crear-transferencia' })"
                class="btn btn-outline-success">Transferencia</button>
        </div>
    </div>
    
</template>

<script setup>
import { useRouter } from 'vue-router';

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import TransaccionFormView from './TransaccionFormView.vue';

const router = useRouter()

const {
    crearIngreso,
} = useTransaccionesComposable()

</script>