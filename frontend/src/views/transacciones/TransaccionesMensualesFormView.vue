<template>
    <ContainerComponent>
        <TransaccionesFiltrosSelectores @cargar="cargarTransaccionesMensuales"/>
        <div class="row">
            <div class="col-2 d-flex align-items-center">
                <DynamicCheckBoxComponent v-model="transaccionesFiltros.EstablecerRango" name="EstablecerRango" @onChange="cargarTransaccionesMensuales">
                    Establecer rango
                </DynamicCheckBoxComponent>
            </div>
            <div class="col">
                <DynamicInputComponent type="month" v-model="transaccionesFiltros.FechaInicialMensual" name="FechaInicialMensual" @onChange="cargarTransaccionesMensuales">
                    Fecha Inicial
                </DynamicInputComponent>
            </div>
            <div class="col">
                <DynamicInputComponent v-if="transaccionesFiltros.EstablecerRango" v-model="transaccionesFiltros.FechaFinalMensual" type="month" name="FechaFinalMensual" @onChange="cargarTransaccionesMensuales">
                    Fecha Final
                </DynamicInputComponent>
            </div>
        </div>
    </ContainerComponent>
</template>

<script setup>
import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import { 
    DynamicInputComponent,
    DynamicCheckBoxComponent,
} from '@/components/inputComponents'

import ContainerComponent from '@/components/ContainerComponent.vue';
import TransaccionesFiltrosSelectores from './TransaccionesFiltrosSelectores.vue';

const {
    transaccionesFiltros,
    
    cargarTransaccionesMensuales,
} = useTransaccionesComposable()

const refresh = async() => {
    await cargarTransaccionesMensuales()
}

refresh()
</script>