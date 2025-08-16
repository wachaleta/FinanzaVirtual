<template>
    <RouterView 
        @onAceptar="router.push({name: 'perfil-listado'})"
        @onCancelar="router.push({name: 'perfil-crear'})"
    />
    <form @submit.prevent="crearPerfil">
        <DynamicModalComponent size="sm"
            @onCancelar="router.push({name: 'perfil-crear-cancelar'})">
            <template v-slot:header>
                Crear Perfil
            </template>
            <template v-slot:body>
                <PerfilFormView v-model="perfil"/>
            </template>
        </DynamicModalComponent>
    </form>
</template>

<script setup>

import { useRouter } from 'vue-router'
import { useErrorsComposable } from '@/composables/useErrorsComposable';
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import PerfilFormView from './PerfilFormView.vue';
import DynamicModalComponent from '@/components/DynamicModalComponent.vue';

const router = useRouter()

const { cleanErrors } = useErrorsComposable()

const {
    perfil,

    crearPerfil,
} = usePerfilesComposable()

const refresh = async() => {
    cleanErrors()
    perfil.value = {}
}

refresh()

</script>
