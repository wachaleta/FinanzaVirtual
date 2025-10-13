<template>
    <RouterView />
    <!-- Formulario para gastos e ingresos -->
    <div class="col-12 mt-3">
        <div class="form-control px-4">
            <div class="row d-flex align-content-center mb-2">
                <form @submit.prevent="editarTransferencia()">
                    <TransferenciaFormView />
                    <div class="row">
                        <div class="col-6">
                            <DynamicButtonComponent type="submit" color="success" icon="edit" style="height: 100%;">
                                Editar Transferencia
                            </DynamicButtonComponent>
                        </div>
                        <div class="col-6 text-end">
                            <DynamicButtonComponent icon="delete" color="danger"
                                @click="router.push({ name: 'transferencia-eliminar' })">
                                Eliminar Transferencia
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
    DynamicButtonComponent
} from '@/components/buttonComponents'

import TransferenciaFormView from './TransferenciaFormView.vue';

const route = useRoute()
const router = useRouter()

const {
    editarTransferencia,

    cargarTransaccionPorId,
} = useTransaccionesComposable()


const refresh = async () => {
    await cargarTransaccionPorId(route.params.idTransaccion)
}

refresh()

</script>
