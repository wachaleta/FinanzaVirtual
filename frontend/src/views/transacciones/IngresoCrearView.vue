<template>
    <form @submit.prevent="crearIngreso">
        <TransaccionFormView/>
    </form>
</template>

<script setup>
import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import TransaccionFormView from './TransaccionFormView.vue';

const {
    crearIngreso,
} = useTransaccionesComposable()

</script>