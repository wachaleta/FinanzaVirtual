<template>
    <form @submit.prevent="crearTransferencia">
        <TransferenciaFormView/>
    </form>
</template>

<script setup>
import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import TransferenciaFormView from './TransferenciaFormView.vue';

const {
    crearTransferencia,
} = useTransaccionesComposable()

</script>