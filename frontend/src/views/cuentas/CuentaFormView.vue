<template>
    <div class="mb-3">
        <DynamicInputComponent name="Nombre" v-model="cuenta.nombre">
            Nombre
        </DynamicInputComponent>
    </div>
    <DynamicCheckBoxComponent name="es_efectivo" v-model="cuenta.es_efectivo">Es cuenta de efectivo?</DynamicCheckBoxComponent>
    <div v-if="cuenta.es_efectivo == true" class="row mt-3">

        <InputGroupComponent v-for="item in listado_efectivo()" v-model="cuentaEfectivo[get_id(item)]" type="number" class="mb-2" name="efectivo">
            {{ $filters.currencyGTQ(item.valor) }}
        </InputGroupComponent>

    </div>
    <div v-else class="mt-3">
        <DynamicInputComponent type="number" min="0" step="0.01" name="saldo_real" v-model="cuenta.saldo_real">Saldo real</DynamicInputComponent>
    </div>
</template>

<script setup>

import { useErrorsComposable } from '@/composables/useErrorsComposable';
import { useCuentasComposable } from '@/composables/useCuentasComposable';
import { 
    DynamicInputComponent,
    InputGroupComponent,
} from '@/components/inputComponents'

import {
    DynamicCheckBoxComponent,
} from '@/components/inputComponents';
import { useEfectivoMonedaComposable } from '@/composables/useEfectivoMonedaComposable';
import { ref } from 'vue';
import CuentaConfirmCancelarEditarModalView from './CuentaConfirmCancelarEditarModalView.vue';

const { cleanErrors } = useErrorsComposable()

const {
    cuenta,
    cuentaEfectivo,
} = useCuentasComposable()

const {
    efectivoMonedaList
} = useEfectivoMonedaComposable()

const refresh = () => {
    cleanErrors()
}

refresh()

const listado_efectivo = () => {
    if(cuenta.value.cuentaefectivo_set?.length > 0){
        return cuenta.value.cuentaefectivo_set
    } else {
        return efectivoMonedaList.value
    }
}

const get_id = (item) => {
    if(cuenta.value.cuentaefectivo_set?.length > 0){
        return item.efectivo_moneda
    } else {
        return item.id
    }
}

</script>