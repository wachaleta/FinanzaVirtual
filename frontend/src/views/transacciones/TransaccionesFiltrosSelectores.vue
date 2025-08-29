<template>
    <div class="row">
        <div class="col">
            <PerfilSelectComponent v-model="transaccionesFiltros.IdPerfiles" :multiple="true" :closeOnSelect="false"
                @onSelect="$emit('cargar')" @onRemove="$emit('cargar')" />
        </div>

        <div class="col">
            <CuentaSelectComponent v-model="transaccionesFiltros.IdCuentas" :multiple="true" :closeOnSelect="false"
                @onSelect="$emit('cargar')" @onRemove="$emit('cargar')" />
        </div>

        <div class="col">
            <CategoriaSelectComponent v-model="transaccionesFiltros.IdCategorias" :multiple="true"
                :closeOnSelect="false" @onSelect="$emit('cargar')" @onRemove="$emit('cargar')" />
        </div>
    </div>
</template>

<script setup>

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable'

import {
    PerfilSelectComponent,
    CuentaSelectComponent,
    CategoriaSelectComponent,
} from '@/components/selectComponents'

defineEmits(['cargar'])

const {
    transaccionesFiltros
} = useTransaccionesComposable()

</script>