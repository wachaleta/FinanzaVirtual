<template>
    <DynamicInputComponent v-model="categoria.Nombre" name="Nombre" v-focus>
        Nombre
    </DynamicInputComponent>
</template>

<script setup>

import { useCategoriasComposable } from '@/composables/useCategoriasComposable'

import {
    DynamicInputComponent,
} from '@/components/inputComponents'

const {
    categoria,
} = useCategoriasComposable()

</script>