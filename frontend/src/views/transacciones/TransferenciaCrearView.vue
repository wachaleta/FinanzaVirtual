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
                class="btn btn-outline-success">Ingreso</button>
        </div>
        <!-- Botón de transferencia -->
        <div class="col-1">
            <button type="button" class="btn btn-success">Transferencia</button>
        </div>
    </div>
    <div class="col-11 px-5 m-4">
        <div class="form-control m-3 px-4">
            <div class="row d-flex align-content-center mb-2">
                <div>
                    <form @submit.prevent="crearTransferencia">
                        <TransferenciaFormView />
                        <button type="submit" class="btn btn-success" id="buttonCrear">Crear Transferencia</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import TransferenciaFormView from './TransferenciaFormView.vue';

const router = useRouter()

const {
    crearTransferencia,
} = useTransaccionesComposable()

</script>