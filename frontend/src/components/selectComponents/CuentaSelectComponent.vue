<template>
    <DynamicSelectComponent
        v-model="model"
        name="IdCuenta"
        valueRef="IdCuenta"
        :items="cuentas"
        :optionText="(item) => item.Nombre + ': ' + $filters.currencyGTQ(item.SaldoTotal)"
    >
        <slot>
            Cuenta
        </slot>
    </DynamicSelectComponent>
</template>

<script setup>
import { useCuentasComposable } from '@/composables/useCuentasComposable';

import DynamicSelectComponent from './DynamicSelectComponent.vue';

const model = defineModel()

const {
    cuentas,

    cargarCuentas
} = useCuentasComposable()

const refresh = async() =>{
    await cargarCuentas()
}

refresh()

</script>