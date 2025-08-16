<template>
    <RouterView/>
    <form @submit.prevent="submitForm">
        <DynamicModalComponent size="sm"
            :showDeleteButton="true"
            @onCancelar="router.push({name: 'perfil-editar-cancelar'})"
            @onEliminar="router.push({name: 'perfil-editar-eliminar'})"
        >
            <template v-slot:header>
                Editar {{ perfil.Nombre }}
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

import { useRouter, useRoute } from 'vue-router'
import { useErrorsComposable } from '@/composables/useErrorsComposable';
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import { DynamicButtonComponent } from '@/components/buttonComponents';

import PerfilFormView from './PerfilFormView.vue';
import DynamicModalComponent from '@/components/DynamicModalComponent.vue';

const router = useRouter()
const route = useRoute()

const { cleanErrors } = useErrorsComposable()

const {
    perfil,

    editarPerfil,
    cargarPerfilPorId,
} = usePerfilesComposable()

const aceptar = () => {
    alert("aceptar")
}

const submitForm = async() => {
    await editarPerfil()
    // router.push({name: 'perfil-listado'})
}

const refresh = async() => {
    cleanErrors()
    await cargarPerfilPorId(route.params.idPerfil)
}

refresh()

</script>
