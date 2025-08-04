<template>
    <TransaccionFormView
        v-model="transaccion"
        tipoTransaccion="Ingreso"
        @submitForm="submitForm"
    />
</template>

<script setup>
import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import TransaccionFormView from './TransaccionFormView.vue';

const {
    transaccion,
} = useTransaccionesComposable()

const submitForm = () => {
    alert("Crear Ingreso")
}

</script>