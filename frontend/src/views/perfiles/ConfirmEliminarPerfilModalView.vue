<template>
    <DynamicModalComponent style="z-index: 99999;"
        size="xs"
        okLabel="Sí, eliminar"
        @onAceptar="eliminarPerfil"
        @onCancelar="router.push({name: 'perfil-editar'})"
    >
        <template v-slot:header>
            Eliminar Perfil
        </template>

        <template v-slot:body>
            Seguro que desea eliminar el perfil <strong>{{ perfil.Nombre }}</strong>?
        </template>
    </DynamicModalComponent>
</template>

<script setup>

import { useRouter } from 'vue-router';
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import DynamicModalComponent from '@/components/DynamicModalComponent.vue';

const router = useRouter()

const {
    perfil,
    eliminarPerfil,
} = usePerfilesComposable()

</script>