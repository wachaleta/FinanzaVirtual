<template>
    <RouterView 
        @onAceptar="router.push({name: 'categoria-listado'})"
        @onCancelar="router.push({name: 'categoria-crear'})"
    />
    <form @submit.prevent="crearCategoria" @keyup.esc="router.push({name: 'categoria-crear-cancelar'})">
        <DynamicModalComponent size="sm"
            @onCancelar="router.push({name: 'categoria-crear-cancelar'})">
            <template v-slot:header>
                Crear Categoria
            </template>
            <template v-slot:body>
                <CategoriaFormView/>
            </template>
        </DynamicModalComponent>
    </form>
</template>

<script setup>

import { useRouter } from 'vue-router'
import { useErrorsComposable } from '@/composables/useErrorsComposable';
import { useCategoriasComposable } from '@/composables/useCategoriasComposable';

import CategoriaFormView from './CategoriaFormView.vue';
import DynamicModalComponent from '@/components/DynamicModalComponent.vue';

const router = useRouter()

const { cleanErrors } = useErrorsComposable()

const {
    categoria,

    crearCategoria,
} = useCategoriasComposable()

const refresh = async() => {
    cleanErrors()
    categoria.value = {}
}

refresh()

</script>
