<template>
    <form @submit.prevent="submitForm">
        <DynamicModalComponent size="sm"
            @onAceptar="aceptar"
            @onCancelar="router.push({name: 'perfil-listado'})">
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
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import PerfilFormView from './PerfilFormView.vue';
import DynamicModalComponent from '@/components/DynamicModalComponent.vue';

const router = useRouter()

const {
    perfil,

    crearPerfil,
} = usePerfilesComposable()

const aceptar = () => {
    alert("aceptar")
}

const submitForm = async() => {
    await crearPerfil()
    // router.push({name: 'perfil-listado'})
}

const refresh = async() => {
    perfil.value = {}
}

refresh()

</script>
