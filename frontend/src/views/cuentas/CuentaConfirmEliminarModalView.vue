<template>
    <DynamicModalComponent style="z-index: 99999;"
        size="xs"
        okLabel="Sí, eliminar"
        @onAceptar="eliminarCuenta"
        @onCancelar="router.push({name: 'cuenta-editar'})"
    >
        <template v-slot:header>
            Eliminar Cuenta
        </template>

        <template v-slot:body>
            Seguro que desea eliminar la cuenta <strong>{{ cuenta.nombre }}</strong>?
        </template>
    </DynamicModalComponent>
</template>

<script setup>

import { useRouter } from 'vue-router';
import { useCuentasComposable } from '@/composables/useCuentasComposable';

import DynamicModalComponent from '@/components/DynamicModalComponent.vue';

const router = useRouter()

const {
    cuenta,
    eliminarCuenta,
} = useCuentasComposable()

</script>