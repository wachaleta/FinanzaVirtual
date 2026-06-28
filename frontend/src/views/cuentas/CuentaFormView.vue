<template>
    <div class="mb-3">
        <DynamicInputComponent name="Nombre" v-model="cuenta.nombre">
            Nombre
        </DynamicInputComponent>
    </div>
    <DynamicCheckBoxComponent name="es_efectivo" v-model="cuenta.es_efectivo">Es cuenta de efectivo?</DynamicCheckBoxComponent>
    <div v-if="cuenta.es_efectivo == true" class="row mt-3">
        <InputGroupComponent v-model="cuenta.bQ100" type="number" class="mb-2" name="bQ100">
            Q100
        </InputGroupComponent>
        
        <InputGroupComponent v-model="cuenta.bQ50" type="number" class="mb-2" name="bQ50">
            Q50
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.bQ20" type="number" class="mb-2" name="bQ20">
            Q20
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.bQ10" type="number" class="mb-2" name="bQ10">
            Q10
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.bQ5" type="number" class="mb-2" name="bQ5">
            Q5
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.m100c" type="number" class="mb-2" name="m100c">
            Q1
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.m50c" type="number" class="mb-2" name="m50c">
            Q0.50
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.m25c" type="number" class="mb-2" name="m25c">
            Q0.25
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.m10c" type="number" class="mb-2" name="m10c">
            Q0.10
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.m5c" type="number" class="mb-2" name="m5c">
            Q0.05
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

const { cleanErrors } = useErrorsComposable()

const {
    cuenta
} = useCuentasComposable()

const refresh = () => {
    cleanErrors()
}

refresh()

</script>