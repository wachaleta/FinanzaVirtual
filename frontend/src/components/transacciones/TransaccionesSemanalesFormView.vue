<template>
    <ContainerComponent>
        <TransaccionesFiltrosSelectores @cargar="cargarTransaccionesSemanales"/>
        <div class="row">
            <div class="col-2 d-flex align-items-center">
                <DynamicCheckBoxComponent v-model="transaccionesFiltros.EstablecerRango" name="rango" @onChange="cargarTransaccionesSemanales">
                Establecer rango
                </DynamicCheckBoxComponent>
            </div>
            <div class="col">
                <DynamicInputComponent type="week" name="FechaInicialSemanal" v-model="transaccionesFiltros.FechaInicialSemanal" @onChange="cargarTransaccionesSemanales">
                    Fecha Inicial
                </DynamicInputComponent>
            </div>
            <div class="col">
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

import ContainerComponent from '../ContainerComponent.vue';

const {
    transaccionesFiltros,

    cargarTransaccionesSemanales,
} = useTransaccionesComposable()

const refresh = async() => {
    await cargarTransaccionesSemanales()
}

refresh()

</script>