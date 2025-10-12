<template>
    <ConfirmModalComponent aceptarLabel="Sí, eliminar"
        @onCancelar="router.push({ name: route.matched[route.matched.length - 2].name })"
        @onAceptar="eliminarTransaccion()" />
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import ConfirmModalComponent from '@/components/ConfirmModalComponent.vue';

const router = useRouter()
const route = useRoute()

const {
    eliminarTransaccion,
} = useTransaccionesComposable()

</script>