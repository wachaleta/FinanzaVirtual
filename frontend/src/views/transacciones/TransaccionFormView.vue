<template>
    <div class="row">
        <div class="col-6">
            <div class="mb-3">
                <DynamicInputComponent v-focus type="number" name="monto" min="0" step="0.01" v-model="transaccion.monto" placeholder="Q 0.00">
                    Monto
                </DynamicInputComponent>
            </div>
        </div>
    
        <div class="col-12 col-sm-6">
            <CategoriaSelectComponent v-model="transaccion.categoria" name="categoria"/>
        </div>
    
        <div class="col-12 col-sm-6">
            <CuentaSelectComponent v-model="transaccion.cuenta_ordenante" name="cuenta_ordenante"/>
        </div>
    
        <div class="col-12 col-sm-6">
            <PerfilSelectComponent v-model="transaccion.perfil_ordenante" name="perfil_ordenante"/>
        </div>

        <div class="col-6">
            <div class="mb-3">
                <DynamicInputComponent type="date" name="fecha" v-model="transaccion.fecha">Fecha:</DynamicInputComponent>
            </div>
        </div>
    
        <div class="col-12 col-sm-6">
            <div class="mb-3">
                <DynamicInputComponent v-model="transaccion.descripcion" name="descripcion" placeholder="Descripción (opcional)">Descripción</DynamicInputComponent>
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