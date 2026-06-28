<template>
    <DynamicSelectComponent
        v-if="cargado"
        v-model="model"
        name="id"
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

import DynamicSelectComponent from './DynamicSelectComponent.vue';
import { ref } from 'vue';

const model = defineModel()
const cargado = ref(false)

const {
    categorias,

    cargarCategorias
} = useCategoriasComposable()

const refresh = async() =>{
    await cargarCategorias()
    cargado.value = true
}

refresh()

</script>