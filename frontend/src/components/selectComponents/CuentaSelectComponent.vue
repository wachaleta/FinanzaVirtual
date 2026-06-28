<template>
    <DynamicSelectComponent
        v-if="cargado"
        v-model="model"
        name="id"
        valueRef="id"
        :items="cuentas"
        :optionText="(item) => item.nombre + ': ' + $filters.currencyGTQ(item.saldo_total)"
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

const props = defineProps({
    cargarItems: {
        type: Boolean,
        default: true
    }
})

const {
    cuentas,
    cuentasFiltros,

    cargarCuentas
} = useCuentasComposable()

const refresh = async() =>{
    if(props.cargarItems){
        cuentasFiltros.value = {
            activo: true
        }
        await cargarCuentas()
    }
    
    cargado.value = true
}

refresh()

</script>