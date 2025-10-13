<template>
    <RouterView/>
    <!-- Formulario para gastos e ingresos -->
    <div class="col-12 mt-3">
        <div class="form-control px-4">
            <div class="row d-flex align-content-center mb-2">
                <form @submit.prevent="submitForm">
                    <TransaccionFormView />
                    <DynamicButtonComponent icon="save" color="success" type="submit">
                        Crear {{ $route.meta.tipoTransaccion }}
                    </DynamicButtonComponent>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable'

import {
    DynamicButtonComponent,
} from '@/components/buttonComponents'

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