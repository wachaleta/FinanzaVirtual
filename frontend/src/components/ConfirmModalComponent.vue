<template>
    <DynamicModalComponent style="z-index: 99999;" size="xs">
        <template #header>
            {{ route.meta.title ?? "Cancelar" }}
        </template>

        <template #body>
            {{ route.meta.subtitle ?? "Seguro que deseas cancelar la acción?" }}
        </template>

        <template #footer>
            <DynamicButtonComponent @click="$emit('onCancelar')" color="danger">No</DynamicButtonComponent>
            <DynamicButtonComponent @click="$emit('onAceptar')" class="ms-2">{{ aceptarLabel }}</DynamicButtonComponent>
        </template>
    </DynamicModalComponent>
</template>

<script setup>

import { useRoute } from 'vue-router'

import DynamicModalComponent from './DynamicModalComponent.vue';

import { DynamicButtonComponent } from '@/components/buttonComponents';

const route = useRoute();

defineEmits(['onAceptar', 'onCancelar'])
const props = defineProps({
    size: {
        type: String,
        default: "xs"
    },

    aceptarLabel: {
        type: String,
        default: "Sí, cancelar"
    },
})
</script>