<template>
    <ConfirmModalComponent
        @onAceptar="router.push({name: 'perfil-listado'})"
        @onCancelar="router.push({name: 'perfil-editar'})"
    />
</template>

<script setup>
import { useRouter } from 'vue-router';
import ConfirmModalComponent from '@/components/ConfirmModalComponent.vue';

const router = useRouter()

</script>