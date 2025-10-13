<template>
    <ContainerComponent>
        <TransaccionesFiltrosSelectores @cargar="cargarTransaccionesDiarias"/>
        <div class="row">
            <div class="col-12 col-sm-12 col-md-2 mb-3 mb-md-0 d-flex align-items-center">
                <DynamicCheckBoxComponent v-model="transaccionesFiltros.EstablecerRango" name="EstablecerRango"
                    @onChange="cargarTransaccionesDiarias">
                    Establecer rango
                </DynamicCheckBoxComponent>
            </div>
            <div class="col-6 col-md-5 ps-md-5 ps-lg-0">
                <DynamicInputComponent v-model="transaccionesFiltros.FechaInicialDiaria" type="date"
                    name="FechaInicialDiaria" @onChange="cargarTransaccionesDiarias">
                    Fecha Inicial
                </DynamicInputComponent>
            </div>
            <div class="col-6 col-md-5">
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