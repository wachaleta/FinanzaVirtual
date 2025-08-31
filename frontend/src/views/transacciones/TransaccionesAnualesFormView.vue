<template>
    <ContainerComponent>
        <TransaccionesFiltrosSelectores @cargar="cargarTransaccionesAnuales"/>
        <div class="row">
            <div class="col-2 d-flex align-items-center">
                <DynamicCheckBoxComponent v-model="transaccionesFiltros.EstablecerRango" name="EstablecerRango" @onChange="cargarTransaccionesAnuales">
                    Establecer rango
                </DynamicCheckBoxComponent>
            </div>
            <div class="col">
                <DynamicInputComponent type="number" v-model="transaccionesFiltros.FechaInicialAnual" name="FechaInicialAnual" @onChange="cargarTransaccionesAnuales">
                    Fecha Inicial
                </DynamicInputComponent>
            </div>
            <div class="col">
                <DynamicInputComponent v-if="transaccionesFiltros.EstablecerRango" v-model="transaccionesFiltros.FechaFinalAnual" type="number" name="FechaFinalAnual" @onChange="cargarTransaccionesAnuales">
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
    
    cargarTransaccionesAnuales,
} = useTransaccionesComposable()

const refresh = async() => {
    await cargarTransaccionesAnuales()
}

refresh()
</script>