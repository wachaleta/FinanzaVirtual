<template>
    <div class="row">
        <div class="col-6">
            <DynamicInputComponent v-focus type="number" name="Monto" min="0" step="0.01" v-model="transaccion.Monto">
                Monto
            </DynamicInputComponent>
        </div>
        <div class="col-6">
            <DynamicInputComponent type="date" v-model="transaccion.Fecha" name="Fecha">Fecha:</DynamicInputComponent>
        </div>
    </div>
    <div class="row my-2">
        <DynamicCheckBoxComponent v-model="transaccion.TransferenciaEntrePerfiles" class="mb-3 ms-2" name="TransferenciaEntrePerfiles">
            Transferir entre perfiles
        </DynamicCheckBoxComponent>

        <div v-if="transaccion.TransferenciaEntrePerfiles == true" class="col-12 col-sm-6">
            <PerfilSelectComponent v-model="transaccion.IdPerfilOrdenante" name="IdPerfilOrdenante">
                De:
            </PerfilSelectComponent>
        </div>
        <div v-else class="col-12 col-sm-6">
            <CuentaSelectComponent v-model="transaccion.IdCuentaOrdenante" name="IdCuentaOrdenante">
                De:
            </CuentaSelectComponent>
        </div>

        <div v-if="transaccion.TransferenciaEntrePerfiles" class="col-12 col-sm-6">
            <PerfilSelectComponent v-model="transaccion.IdPerfilBeneficiario" name="IdPerfilBeneficiario">
                Para:
            </PerfilSelectComponent>
        </div>
        <div v-else class="col-12 col-sm-6">
            <CuentaSelectComponent v-model="transaccion.IdCuentaBeneficiaria" name="IdCuentaBeneficiaria">
                Para:
            </CuentaSelectComponent>
        </div>
    </div>
    <!-- Categorias -->
    <div class="row">
        <div class="col-12 col-sm-6">
            <CategoriaSelectComponent v-model="transaccion.IdCategoria" name="IdCategoria" />
        </div>
        <div class="col-12 col-sm-6">
            <DynamicInputComponent v-model="transaccion.Descripcion" name="Descripcion">
                Descripción
            </DynamicInputComponent>
        </div>
    </div>
</template>

<script setup>
import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import { DynamicInputComponent } from '@/components/inputComponents'

import {
    PerfilSelectComponent,
    CuentaSelectComponent,
    CategoriaSelectComponent,
} from '@/components/selectComponents'

import {
    DynamicCheckBoxComponent,
} from '@/components/inputComponents';

const { transaccion } = useTransaccionesComposable()

</script>