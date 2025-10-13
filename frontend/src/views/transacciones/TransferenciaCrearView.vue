<template>
    <!-- Botones de selección de transacción -->
    <div class="row m-0">
        <!-- Botón de gasto -->
        <div class="col-6 col-sm-4 d-flex justify-content-evenly">
            <button type="button" class="btn btn-outline-success"
                @click="router.push({ name: 'transaccion-crear-gasto' })">Gasto</button>
        </div>
        <!-- Botón de ingreso -->
        <div class="col-6 col-sm-4 d-flex justify-content-evenly">
            <button type="button" @click="router.push({ name: 'transaccion-crear-ingreso' })"
                class="btn btn-outline-success">Ingreso</button>
        </div>
        <!-- Botón de transferencia -->
        <div class="col-sm-4 mt-3 mt-sm-0 d-flex justify-content-evenly">
            <button type="button" class="btn btn-success">Transferencia</button>
        </div>
    </div>
    <div class="col-12 mt-3">
        <div class="form-control px-4">
            <div class="row d-flex align-content-center mb-2">
                <form @submit.prevent="crearTransferencia">
                    <TransferenciaFormView />
                    <DynamicButtonComponent icon="save" color="success" type="submit">
                        Crear Transferencia
                    </DynamicButtonComponent>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import {
    DynamicButtonComponent,
} from '@/components/buttonComponents'

import TransferenciaFormView from './TransferenciaFormView.vue';

const router = useRouter()

const {
    crearTransferencia,
} = useTransaccionesComposable()

</script>