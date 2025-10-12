<template>
    <RouterView/>
    <!-- Formulario para gastos e ingresos -->
    <div class="col-11 px-5 m-4">
        <div class="form-control m-3 px-4">
            <div class="row d-flex align-content-center mb-2">
                <form @submit.prevent="submitForm">
                    <TransaccionFormView />
                    <div class="row">
                        <div class="col-6">
                            <DynamicButtonComponent type="submit" icon="edit" color="success">
                                Editar {{ $route.meta.tipoTransaccion }}
                            </DynamicButtonComponent>
                        </div>
                        <div class="col-6 text-end">
                            <DynamicButtonComponent icon="delete" color="danger" @click="router.push({name: `${route.meta.tipoTransaccion.toLowerCase()}-eliminar`})">
                                Eliminar {{ $route.meta.tipoTransaccion }}
                            </DynamicButtonComponent>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import {
    DynamicButtonComponent,
} from '@/components/buttonComponents'
import TransaccionFormView from './TransaccionFormView.vue';


const route = useRoute()
const router = useRouter()

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
