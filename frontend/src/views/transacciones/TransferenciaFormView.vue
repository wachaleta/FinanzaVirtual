<template>
    <div class="row">
        <div class="col-12 col-sm-6">
            <div class="mb-3">
                <DynamicInputComponent v-model="transaccion.monto" v-focus type="number" name="monto" min="0" step="0.01" placeholder="Q 0.00">
                    Monto
                </DynamicInputComponent>
            </div>
        </div>

        <div class="col-12 col-sm-6">
            <CategoriaSelectComponent v-model="transaccion.categoria" name="categoria" />
        </div>
    </div>
    <div class="row my-2">
        <DynamicCheckBoxComponent v-model="transaccion.transferencia_entre_perfiles" class="mb-3 ms-2" name="transferencia_entre_perfiles">
            Transferir entre perfiles
        </DynamicCheckBoxComponent>

        <div v-if="transaccion.transferencia_entre_perfiles == true" class="col-12 col-sm-6">
            <PerfilSelectComponent v-model="transaccion.perfil_ordenante" :cargar-items="false" name="perfil_ordenante">
                De:
            </PerfilSelectComponent>
        </div>
        <div v-else class="col-12 col-sm-6">
            <CuentaSelectComponent v-model="transaccion.cuenta_ordenante" :cargar-items="false" name="cuenta_ordenante">
                De:
            </CuentaSelectComponent>
        </div>

        <div v-if="transaccion.transferencia_entre_perfiles" class="col-12 col-sm-6">
            <PerfilSelectComponent v-model="transaccion.perfil_beneficiario" :cargar-items="false" name="perfil_beneficiario">
                Para:
            </PerfilSelectComponent>
        </div>
        <div v-else class="col-12 col-sm-6">
            <CuentaSelectComponent v-model="transaccion.cuenta_beneficiaria" :cargar-items="false" name="cuenta_beneficiaria">
                Para:
            </CuentaSelectComponent>
        </div>
    </div>
    <!-- Categorias -->
    <div class="row">
        
        <div class="col-12 col-sm-6">
            <div class="mb-3">
                <DynamicInputComponent type="date" v-model="transaccion.fecha" name="Fecha">Fecha:</DynamicInputComponent>
            </div>
        </div>
        <div class="col-12 col-sm-6">
            <div class="mb-3">
                <DynamicInputComponent v-model="transaccion.descripcion" name="descripcion" placeholder="Descripción (opcional)">
                    Descripción
                </DynamicInputComponent>
            </div>
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
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';
import { useCuentasComposable } from '@/composables/useCuentasComposable';

const { transaccion } = useTransaccionesComposable()

const {
    perfilesFiltros,

    cargarPerfiles,
} = usePerfilesComposable()

const {
    cuentasFiltros,
    cargarCuentas,
} = useCuentasComposable()

const refresh = async () => {
    perfilesFiltros.value = {
        activo: true,
    }
    cargarPerfiles()
    
    cuentasFiltros.value = {
        activo: true
    }
    cargarCuentas()

    transaccion.value.transferencia_entre_perfiles = true
}

refresh()

</script>