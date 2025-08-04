<template>
    <DynamicSelectComponent
        v-model="model"
        :items="cuentas"
        :optionText="(item) => item.nombre + ': Q' + item.saldo_total"
        valueRef="id"
    >
        <slot>
            Cuenta
        </slot>
    </DynamicSelectComponent>
</template>

<script setup>
import { useCuentasComposable } from '@/composables/useCuentasComposable';

import DynamicSelectComponent from '@/components/formComponents/DynamicSelectComponent.vue';

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