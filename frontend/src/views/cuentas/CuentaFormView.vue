<template>
    <DynamicInputComponent name="Nombre" v-model="cuenta.Nombre">
        Nombre
    </DynamicInputComponent>
    <DynamicCheckBoxComponent name="EsEfectivo" v-model="cuenta.EsEfectivo">Es cuenta de efectivo?</DynamicCheckBoxComponent>
    <div v-if="cuenta.EsEfectivo == true" class="row mt-3">
        <InputGroupComponent v-model="cuenta.BQ100" type="number" class="mb-2" name="BQ100">
            Q100
        </InputGroupComponent>
        
        <InputGroupComponent v-model="cuenta.BQ50" type="number" class="mb-2" name="BQ50">
            Q50
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.BQ20" type="number" class="mb-2" name="BQ20">
            Q20
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.BQ10" type="number" class="mb-2" name="BQ10">
            Q10
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.BQ5" type="number" class="mb-2" name="BQ5">
            Q5
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.M100c" type="number" class="mb-2" name="M100c">
            Q1
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.M50c" type="number" class="mb-2" name="M50c">
            Q0.50
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.M25c" type="number" class="mb-2" name="M25c">
            Q0.25
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.M10c" type="number" class="mb-2" name="M10c">
            Q0.10
        </InputGroupComponent>

        <InputGroupComponent v-model="cuenta.M5c" type="number" class="mb-2" name="M5c">
            Q0.05
        </InputGroupComponent>
    </div>
    <DynamicInputComponent v-else type="number" min="0" step="0.01" name="SaldoReal" v-model="cuenta.SaldoReal">Saldo real</DynamicInputComponent>
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