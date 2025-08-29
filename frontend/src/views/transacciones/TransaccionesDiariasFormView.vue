<template>
    <ContainerComponent>
        <TransaccionesFiltrosSelectores @cargar="cargarTransaccionesDiarias"/>
        <div class="row">
            <div class="col-2 d-flex align-items-center">
                <DynamicCheckBoxComponent v-model="transaccionesFiltros.EstablecerRango" name="EstablecerRango"
                    @onChange="cargarTransaccionesDiarias">
                    Establecer rango
                </DynamicCheckBoxComponent>
            </div>
            <div class="col">
                <DynamicInputComponent v-model="transaccionesFiltros.FechaInicialDiaria" type="date"
                    name="FechaInicialDiaria" @onChange="cargarTransaccionesDiarias">
                    Fecha Inicial
                </DynamicInputComponent>
            </div>
            <div class="col">
                <DynamicInputComponent v-if="transaccionesFiltros.EstablecerRango"
                    v-model="transaccionesFiltros.FechaFinalDiaria" type="date" name="FechaFinalDiaria"
                    @onChange="cargarTransaccionesDiarias">
                    Fecha Final
                </DynamicInputComponent>
            </div>
        </div>
    </ContainerComponent>
</template>

<script setup>
import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import TransaccionesFiltrosSelectores from './TransaccionesFiltrosSelectores.vue';

import {
    DynamicInputComponent,
    DynamicCheckBoxComponent,
} from '@/components/inputComponents'

import ContainerComponent from '@/components/ContainerComponent.vue';

const {
    transaccionesFiltros,
    cargarTransaccionesDiarias
} = useTransaccionesComposable()

const refresh = async() => {
    await cargarTransaccionesDiarias()
}

refresh()
</script>