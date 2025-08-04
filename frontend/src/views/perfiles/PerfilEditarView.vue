<template>
    <form @submit.prevent="submitForm">
        <DynamicModalComponent size="sm"
            @onAceptar="aceptar"
            >
            <template v-slot:header>
                Editar Perfil
            </template>
            <template v-slot:body>
                <PerfilFormView v-model="perfil"/>
            </template>
            <template v-slot:footer>
                <DynamicButtonComponent @click="eliminar" color="danger">Eliminar</DynamicButtonComponent>
                <DynamicButtonComponent @click="router.push({name: 'perfil-listado'})" color="danger" class="ms-2">Cancelar</DynamicButtonComponent>
                <DynamicButtonComponent type="submit" class="ms-2">Guardar</DynamicButtonComponent>
            </template>
        </DynamicModalComponent>
    </form>
</template>

<script setup>

import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import PerfilFormView from './PerfilFormView.vue';
import DynamicModalComponent from '@/components/DynamicModalComponent.vue';
import DynamicButtonComponent from '@/components/formComponents/DynamicButtonComponent.vue';

const router = useRouter()
const route = useRoute()

const {
    perfil,

    editarPerfil,
    eliminarPerfil,
    cargarPerfilPorId,
} = usePerfilesComposable()

const eliminar = async() => {
    await eliminarPerfil()
    router.push({name: 'perfil-listado'})
}

const aceptar = () => {
    alert("aceptar")
}

const submitForm = async() => {
    await editarPerfil()
    router.push({name: 'perfil-listado'})
}

const refresh = async() => {
    await cargarPerfilPorId(route.params.idPerfil)
}

refresh()

</script>
