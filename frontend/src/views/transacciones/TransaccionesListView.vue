<template>
    <h3 class="ms-4">Saldos</h3>
    <div class="row mb-4">
        <div class="col-12 col-sm-6 col-md-4 mt-3">
            <CardComponent color="success">
                <template v-slot:header>
                    Entradas
                </template>
                <template v-slot:body>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(transacciones.TotalEntradas) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>
        <div class="col-12 col-sm-6 col-md-4 mt-3">
            <CardComponent color="danger">
                <template v-slot:header>
                    Salidas
                </template>
                <template v-slot:body>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(transacciones.TotalSalidas) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>
        <div class="col-12 col-md-4 mt-3">
            <CardComponent :color="transacciones.TotalBalance < 0 ? 'danger' : 'success'">
                <template v-slot:header>
                    Balance
                </template>
                <template v-slot:body>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(transacciones.TotalBalance) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>
    </div>

    <h3 class="ms-4">Filtros</h3>

    <div class="row mb-5">
        <div class="col-6 col-sm-3 col-md-2">
            <PanelNavItemComponent to="transaccion-listado-diario" class="me-2">
                Diario
            </PanelNavItemComponent>
        </div>

        <div class="col-6 col-sm-3 col-md-2">
            <PanelNavItemComponent to="transaccion-listado-semanal" class="me-2">
                Semanal
            </PanelNavItemComponent>
        </div>

        <div class="col-6 col-sm-3 col-md-2">
            <PanelNavItemComponent to="transaccion-listado-mensual" class="me-2">
                Mensual
            </PanelNavItemComponent>
        </div>

        <div class="col-6 col-sm-3 col-md-2">
            <PanelNavItemComponent to="transaccion-listado-anual" class="me-2">
                Anual
            </PanelNavItemComponent>
        </div>
        <RouterView/>

    </div>

    <h3 class="ms-4">Transacciones</h3>

    <div class="row">
        <div v-for="transaccion in transacciones.Items" class="col-12  col-md-6 col-lg-4 mb-3">
            <CardComponent :color="getColorTransaccion(transaccion)" @click="editarTransaccion(transaccion)">
                <template v-slot:header>
                    {{ transaccion.ordenante_nombre }} {{ transaccion.beneficiario_nombre }}
                </template>
                <template #fecha>
                    <div>
                        {{ transaccion.Fecha }}
                    </div>
                    <div>
                        {{ transaccion.CategoriaNombre }}
                    </div>
                </template>
                <template v-slot:descripcion>
                    <span>
                        {{ transaccion.Descripcion }}
                    </span>
                </template>
                <template v-slot:body>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(transaccion.Monto) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>
    </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';

import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable';

import { PanelNavComponent, PanelNavItemComponent } from '@/components/panelNav';

import CardComponent from '@/components/CardComponent.vue';

const route = useRoute()
const router = useRouter()

const {
    transacciones,
} = useTransaccionesComposable()

const getColorTransaccion = (transaccion) => {
    if (transaccion.IdPerfilOrdenante == null && transaccion.IdCuentaOrdenante == null) {
        return 'success'
    }

    if (transaccion.IdPerfilBeneficiario == null && transaccion.IdCuentaBeneficiaria == null) {
        return 'danger'
    }

    return 'info'
}

const editarTransaccion = (transaccion) => {
    router.push(
        {
            name: getTransaccionEditarRoute(transaccion),
            params: {
                idTransaccion: transaccion.IdTransaccion
            },
            query: {
                next: route.name
            }
        }
    )
}

const getTransaccionEditarRoute = (transaccion) => {
    if (transaccion.IdPerfilOrdenante == null && transaccion.IdCuentaOrdenante == null) {
        return 'ingreso-editar'
    }

    if (transaccion.IdPerfilBeneficiario == null && transaccion.IdCuentaBeneficiaria == null) {
        return 'gasto-editar'
    }

    return 'transferencia-editar'
}

</script>