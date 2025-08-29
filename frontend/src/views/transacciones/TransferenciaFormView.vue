<template>
    <div class="row">
        <div class="col-6">
            <DynamicInputComponent type="number" min="1" v-model="transaccion.Monto" name="Monto">
                Monto
            </DynamicInputComponent>
        </div>
        <div class="col-6">
            <DynamicInputComponent type="date" v-model="transaccion.Fecha" name="Fecha">Fecha:</DynamicInputComponent>
        </div>
    </div>
    <div class="row my-2">
        <!-- Ordenante -->
        <DynamicCheckBoxComponent v-model="transaccion.TransferenciaEntrePerfiles" name="TransferenciaEntrePerfiles">
            Transferir entre perfiles
        </DynamicCheckBoxComponent>
        <div class="col border">
            <div class="row">
                <div class="col-1">
                    <p>De:</p>
                </div>
            </div>
            <!-- Perfil -->
            <div v-if="transaccion.TransferenciaEntrePerfiles == true" class="row">
                <PerfilSelectComponent v-model="transaccion.IdPerfilOrdenante" name="IdPerfilOrdenante"/>
            </div>
            <!-- Cuenta -->
            <div v-else class="row">
                <CuentaSelectComponent v-model="transaccion.IdCuentaOrdenante" name="IdCuentaOrdenante"/>
            </div>
        </div>

        <!-- Beneficiario -->
        <div class="col border ms-2">
            <div class="row">
                <div class="col-1">
                    <p>Para:</p>
                </div>
            </div>
            <!-- Perfil -->
            <div v-if="transaccion.TransferenciaEntrePerfiles" class="row">
                <PerfilSelectComponent v-model="transaccion.IdPerfilBeneficiario" name="IdPerfilBeneficiario"/>
            </div>
            <!-- Cuenta -->
            <div v-else class="row">
                <CuentaSelectComponent v-model="transaccion.IdCuentaBeneficiaria" name="IdCuentaBeneficiaria"/>
            </div>
        </div>
    </div>
    <!-- Categorias -->
    <div class="row">
        <div class="col-6">
            <CategoriaSelectComponent v-model="transaccion.IdCategoria" name="IdCategoria"/>
        </div>
        <div class="col-6">
            <DynamicInputComponent v-model="transaccion.Descripcion" name="Descripcion">Descripción</DynamicInputComponent>
        </div>
    </div>
    <div>
        <button type="submit" class="btn btn-success">Crear Transferencia</button>
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