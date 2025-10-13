<template>
    <ContainerComponent>
        <TransaccionesFiltrosSelectores @cargar="cargarTransaccionesMensuales"/>
        <div class="row">
            <div class="col-12 col-sm-12 col-md-2 mb-3 mb-md-0 d-flex align-items-center">
                <DynamicCheckBoxComponent v-model="transaccionesFiltros.EstablecerRango" name="EstablecerRango" @onChange="cargarTransaccionesMensuales">
                    Establecer rango
                </DynamicCheckBoxComponent>
            </div>
            <div class="col-6 col-md-5 ps-md-5 ps-lg-0">
                <DynamicInputComponent type="month" v-model="transaccionesFiltros.FechaInicialMensual" name="FechaInicialMensual" @onChange="cargarTransaccionesMensuales">
                    Fecha Inicial
                </DynamicInputComponent>
            </div>
            <div class="col-6 col-md-5">
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