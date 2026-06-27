<template>
    <div class="row">
        <div class="col-6">
            <div class="mb-3">
                <DynamicInputComponent v-focus type="number" name="Monto" min="0" step="0.01" v-model="transaccion.Monto">
                    Monto
                </DynamicInputComponent>
            </div>
        </div>
    
        <div class="col-6">
            <div class="mb-3">
                <DynamicInputComponent type="date" name="Fecha" v-model="transaccion.Fecha">Fecha:</DynamicInputComponent>
            </div>
        </div>
    
        <div class="col-12 col-sm-6">
            <CuentaSelectComponent v-model="transaccion.IdCuentaOrdenante" name="IdCuentaOrdenante"/>
        </div>
    
        <div class="col-12 col-sm-6">
            <PerfilSelectComponent v-model="transaccion.IdPerfilOrdenante" name="IdPerfilOrdenante"/>
        </div>
    
        <div class="col-12 col-sm-6">
            <CategoriaSelectComponent v-model="transaccion.IdCategoria" name="IdCategoria"/>
        </div>
    
        <div class="col-12 col-sm-6">
            <div class="mb-3">
                <DynamicInputComponent v-model="transaccion.Descripcion" name="descripcion">Descripción</DynamicInputComponent>
            </div>
        </div>
    
    </div>
</template>

<script setup>

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable'

import {
    DynamicInputComponent
} from '@/components/inputComponents'

import {
    PerfilSelectComponent,
    CuentaSelectComponent,
    CategoriaSelectComponent,
} from '@/components/selectComponents'

const { transaccion } = useTransaccionesComposable()

</script>