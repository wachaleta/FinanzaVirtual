<template>
    <RouterView/>
    <!-- Formulario para gastos e ingresos -->
    <div class="col-11 px-5 m-4">
        <div class="form-control m-3 px-4">
            <div class="row d-flex align-content-center mb-2">
                <div>
                    <form @submit.prevent="submitForm">
                        <TransaccionFormView />
                        <button type="submit" class="btn btn-success" id="buttonCrear">Crear {{ $route.meta.tipoTransaccion }}</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable'

import TransaccionFormView from './TransaccionFormView.vue'

const router = useRouter()
const route = useRoute()

const { transaccion } = useTransaccionesComposable()

const {
    crearGasto,
    crearIngreso,
} = useTransaccionesComposable()

const submitForm = async() => {
    if(route.meta.tipoTransaccion == "Gasto"){
        await crearGasto()
    }
    else if(route.meta.tipoTransaccion == "Ingreso"){
        await crearIngreso()
    }
}

const refresh = () => {
    const fecha = transaccion.value.Fecha
    transaccion.value = {}
    transaccion.value.Fecha = fecha
}

refresh()

</script>