<template>
    <ContainerComponent>
        <TransaccionesFiltrosSelectores @cargar="cargarTransaccionesSemanales"/>
        <div class="row">
            <div class="col-12 col-sm-12 col-md-2 mb-3 mb-md-0 d-flex align-items-center">
                <DynamicCheckBoxComponent v-model="transaccionesFiltros.EstablecerRango" name="rango" @onChange="cargarTransaccionesSemanales">
                Establecer rango
                </DynamicCheckBoxComponent>
            </div>
            <div class="col-6 col-md-5 ps-md-5 ps-lg-0">
                <DynamicInputComponent type="week" name="FechaInicialSemanal" v-model="transaccionesFiltros.FechaInicialSemanal" @onChange="cargarTransaccionesSemanales">
                    Fecha Inicial
                </DynamicInputComponent>
            </div>
            <div class="col-6 col-md-5">
                <DynamicInputComponent v-if="transaccionesFiltros.EstablecerRango" v-model="transaccionesFiltros.FechaFinalSemanal" type="week" name="FechaFinalSemanal" @onChange="cargarTransaccionesSemanales">
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

    cargarTransaccionesSemanales,
} = useTransaccionesComposable()

const refresh = async() => {
    await cargarTransaccionesSemanales()
}

refresh()

</script>