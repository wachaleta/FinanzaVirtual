<template>
    <form @submit.prevent="crearGasto">
        <TransaccionFormView/>
    </form>
</template>

<script setup>
import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import TransaccionFormView from './TransaccionFormView.vue';

const {
    crearGasto,
} = useTransaccionesComposable()

</script>