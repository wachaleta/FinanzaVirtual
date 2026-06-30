<template>
    <DynamicSelectComponent
        v-if="cargado"
        v-model="model"
        name="id"
        valueRef="id"
        :multiple="multiple"
        :close-on-select="closeOnSelect"
        :items="perfiles"
        :optionText="(item) => item.nombre + ': ' + $filters.currencyGTQ(item.saldo)"
    >
        <slot>
            Perfil
        </slot>
    </DynamicSelectComponent>
</template>1

<script setup>
import { ref } from 'vue'
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import DynamicSelectComponent from './DynamicSelectComponent.vue';

const model = defineModel()
const cargado = ref(false)

const props = defineProps({
    multiple:{
        type: Boolean,
        default: false
    },

    closeOnSelect:{
        type: Boolean,
        default: true
    },

    cargarItems:{
        type: Boolean,
        default: true
    },
})

const {
    perfiles,
    perfilesFiltros,

    cargarPerfiles
} = usePerfilesComposable()

const refresh = async() =>{
    if(props.cargarItems){
        perfilesFiltros.value = {
            activo: true,
        }
        await cargarPerfiles()
    }

    cargado.value = true
}

refresh()

</script>