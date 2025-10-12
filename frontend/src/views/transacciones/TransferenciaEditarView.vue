<template>
    <RouterView/>
    <!-- Formulario para gastos e ingresos -->
    <div class="col-11 px-5 m-4">
        <div class="form-control m-3 px-4">
            <div class="row d-flex align-content-center mb-2">
                <div>
                    <form @submit.prevent="editarTransferencia()">
                        <TransferenciaFormView />
                        <button type="submit" class="btn btn-success" id="buttonCrear">Editar Transferencia</button>
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
import TransferenciaFormView from './TransferenciaFormView.vue';

const route = useRoute()

const {
    transaccion,

    editarGasto,
    editarIngreso,
    editarTransferencia,

    cargarTransaccionPorId,
} = useTransaccionesComposable()


const refresh = async () => {
    await cargarTransaccionPorId(route.params.idTransaccion)

    // if (transaccion.value.IdPerfilBeneficiario) {
    //     transaccion.value.IdPerfilOrdenante = transaccion.value.IdPerfilBeneficiario
    //     transaccion.value.IdCuentaOrdenante = transaccion.value.IdCuentaBeneficiaria

    //     transaccion.value.IdPerfilBeneficiario = null
    //     transaccion.value.IdCuentaBeneficiaria = null
    // }
}

refresh()

</script>
