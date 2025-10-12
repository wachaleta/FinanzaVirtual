<template>
    <RouterView/>
    <!-- Formulario para gastos e ingresos -->
    <div class="col-11 px-5 m-4">
        <div class="form-control m-3 px-4">
            <div class="row d-flex align-content-center mb-2">
                <div>
                    <form @submit.prevent="submitForm">
                        <TransaccionFormView />
                        <button type="submit" class="btn btn-success" id="buttonCrear">Editar {{ $route.meta.tipoTransaccion }}</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import TransaccionFormView from './TransaccionFormView.vue';

const route = useRoute()

const {
    transaccion,

    editarGasto,
    editarIngreso,

    cargarTransaccionPorId,
} = useTransaccionesComposable()

const submitForm = async () => {
    if(route.meta.tipoTransaccion == "Gasto"){
        await editarGasto()
    }

    else if(route.meta.tipoTransaccion == "Ingreso"){
        await editarIngreso()
    }
}

const refresh = async () => {
    await cargarTransaccionPorId(route.params.idTransaccion)

    if (transaccion.value.IdPerfilBeneficiario) {
        transaccion.value.IdPerfilOrdenante = transaccion.value.IdPerfilBeneficiario
        transaccion.value.IdCuentaOrdenante = transaccion.value.IdCuentaBeneficiaria

        transaccion.value.IdPerfilBeneficiario = null
        transaccion.value.IdCuentaBeneficiaria = null
    }
}

refresh()

</script>
