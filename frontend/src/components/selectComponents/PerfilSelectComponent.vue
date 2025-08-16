<template>
    <DynamicSelectComponent
        v-model="model"
        :items="perfiles"
        :optionText="(item) => item.Nombre + ': Q' + item.Saldo"
        valueRef="id"
    >
        <slot>
            Perfil
        </slot>
    </DynamicSelectComponent>
</template>

<script setup>
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import DynamicSelectComponent from './DynamicSelectComponent.vue';

const model = defineModel()

const {
    perfiles,

    cargarPerfiles
} = usePerfilesComposable()

const refresh = async() =>{
    await cargarPerfiles()
}

refresh()

</script>