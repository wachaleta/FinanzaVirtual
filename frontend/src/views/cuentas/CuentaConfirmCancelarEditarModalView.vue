<template>
    <ConfirmModalComponent
        @onAceptar="router.push({name: 'cuenta-listado'})"
        @onCancelar="router.push({name: 'cuenta-editar'})"
    />
</template>

<script setup>

import { useRouter } from 'vue-router';

import ConfirmModalComponent from '@/components/ConfirmModalComponent.vue';

const router = useRouter()

</script>