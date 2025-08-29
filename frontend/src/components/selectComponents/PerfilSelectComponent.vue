<template>
    <DynamicSelectComponent
        v-model="model"
        name="IdPerfil"
        valueRef="IdPerfil"
        :multiple="multiple"
        :close-on-select="closeOnSelect"
        :items="perfiles"
        :optionText="(item) => item.Nombre + ': ' + $filters.currencyGTQ(item.Saldo)"
    >
        <slot>
            Perfil
        </slot>
    </DynamicSelectComponent>
</template>1

<script setup>
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import DynamicSelectComponent from './DynamicSelectComponent.vue';

const model = defineModel()

defineProps({
    multiple:{
        type: Boolean,
        default: false
    },

    closeOnSelect:{
        type: Boolean,
        default: true
    }
})

const {
    perfiles,

    cargarPerfiles
} = usePerfilesComposable()

const refresh = async() =>{
    await cargarPerfiles()
}

refresh()

</script>