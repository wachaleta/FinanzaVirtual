<template>
    <DynamicSelectComponent
        v-model="model"
        :items="categorias"
        :optionText="(item) => item.nombre"
        valueRef="id"
    >
        <slot>
            Categoría
        </slot>
    </DynamicSelectComponent>
</template>

<script setup>
import { useCategoriasComposable } from '@/composables/useCategoriasComposable';

import DynamicSelectComponent from '@/components/formComponents/DynamicSelectComponent.vue';

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