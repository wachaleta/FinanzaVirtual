<template>
    <DynamicSelectComponent
        v-if="cargado"
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
import { ref } from 'vue';

const model = defineModel()
const cargado = ref(false)

const {
    cuentas,

    cargarCuentas
} = useCuentasComposable()

const refresh = async() =>{
    await cargarCuentas()
    cargado.value = true
}

refresh()

</script>