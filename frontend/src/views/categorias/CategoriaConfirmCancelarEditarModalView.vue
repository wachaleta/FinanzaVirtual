<template>
    <ConfirmModalComponent
        @onAceptar="router.push({name: 'categoria-listado'})"
        @onCancelar="router.push({name: 'categoria-editar'})"
    />
</template>

<script setup>
import { useRouter } from 'vue-router';

import ConfirmModalComponent from '@/components/ConfirmModalComponent.vue';

const router = useRouter()

</script>