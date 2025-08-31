<template>
    <RouterView/>
    <form @submit.prevent="submitForm">
        <DynamicModalComponent size="sm"
            :showDeleteButton="true"
            @onCancelar="router.push({name: 'perfil-editar-cancelar'})"
            @onEliminar="router.push({name: 'perfil-editar-eliminar'})"
        >
            <template v-slot:header>
                Editar {{ Nombre }}
            </template>
            <template v-slot:body>
                <PerfilFormView v-model="perfil"/>
            </template>
            <!-- <template v-slot:footer>
                <DynamicButtonComponent @click="router.push({name: 'perfil-editar-eliminar'})" color="danger">Eliminar</DynamicButtonComponent>
                <DynamicButtonComponent @click="router.push({name: 'perfil-editar-cancelar'})" color="danger" class="ms-2">Cancelar</DynamicButtonComponent>
                <DynamicButtonComponent type="submit" class="ms-2">Guardar</DynamicButtonComponent>
            </template> -->
        </DynamicModalComponent>
    </form>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router'

import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import PerfilFormView from './PerfilFormView.vue';
import DynamicModalComponent from '@/components/DynamicModalComponent.vue';

const router = useRouter()
const route = useRoute()
const Nombre = ref("")

const {
    perfil,

    editarPerfil,
    cargarPerfilPorId,
} = usePerfilesComposable()

const submitForm = async() => {
    await editarPerfil()
}

const refresh = async() => {
    await cargarPerfilPorId(route.params.idPerfil)
    Nombre.value = perfil.value.Nombre
}

refresh()

</script>
