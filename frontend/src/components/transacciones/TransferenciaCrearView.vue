<template>
    <TransferenciaFormView
        v-model="transaccion"
        @submitForm="submitForm"
    />
</template>

<script setup>
import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import TransferenciaFormView from './TransferenciaFormView.vue';

const {
    transaccion,
} = useTransaccionesComposable()

const submitForm = () => {
    alert("Crear Transferencia")
}

console.log("transaccion.value")
console.log(transaccion.value)

</script>