<template>
    <RouterView/>

    <div class="row m-0">
        <div class="col-7">
            <div class="ms-1">
                <h3>Categorías</h3>
                <h6>Etiquetas para dividir las transacciones</h6>
            </div>
        </div>
        <div class="col-5 text-end">
            <ButtonCrearComponent @click="router.push({name: 'categoria-crear'})" class="mt-4"> Crear Categoría </ButtonCrearComponent>
        </div>
    </div>

    <div class="row mt-3">
        <div v-for="categoria in categorias" class="col-6 col-sm-4 col-md-3 mb-4">
            <ContainerComponent @click="router.push({name: 'categoria-editar', params:{ idCategoria: categoria.IdCategoria}})">
                <span> {{ categoria.Nombre }}</span>
            </ContainerComponent>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

import { useCategoriasComposable } from '@/composables/useCategoriasComposable';

import ContainerComponent from '@/components/ContainerComponent.vue';

import {
    ButtonCrearComponent,
} from '@/components/buttonComponents'

const router = useRouter()

const {
    categorias,

    cargarCategorias,
} = useCategoriasComposable()

const refresh = async() => {
    await cargarCategorias()
}

refresh()

</script>