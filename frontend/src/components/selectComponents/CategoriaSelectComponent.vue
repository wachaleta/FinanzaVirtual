<template>
    <DynamicSelectComponent
        v-model="model"
        name="IdCategoria"
        :items="categorias"
        :optionText="(item) => item.Nombre"
        valueRef="IdCategoria"
    >
        <slot>
            Categoría
        </slot>
    </DynamicSelectComponent>
</template>

<script setup>
import { useCategoriasComposable } from '@/composables/useCategoriasComposable';

import DynamicSelectComponent from './DynamicSelectComponent.vue';

const model = defineModel()

const {
    categorias,

    cargarCategorias
} = useCategoriasComposable()

const refresh = async() =>{
    await cargarCategorias()
}

refresh()

</script>