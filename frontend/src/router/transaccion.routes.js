import { useTransaccionesComposable } from '@/composables/useTransaccionesComposable'

import {
    TransaccionesListView,
    TransaccionesDiariasFormView,
    TransaccionesSemanalesFormView,
    TransaccionesMensualesFormView,
    TransaccionesAnualesFormView,

    TransaccionCrearView,
    GastoCrearView,
    IngresoCrearView,
    TransferenciaCrearView,
} from '@/components/transacciones'

export default [
    { path: '/', redirect: { name: 'transaccion-crear' } },
    {
        path: '/transaccion',
        name: 'transaccion',
        redirect: { name: 'transaccion-listado' },
        children: [
            {
                path: 'listado',
                name: 'transaccion-listado',
                component: TransaccionesListView,
                redirect: {name: 'transaccion-listado-diario'},
                children: [
                    {
                        path: 'diario',
                        name: 'transaccion-listado-diario',
                        component: TransaccionesDiariasFormView,
                    },
                    {
                        path: 'semanal',
                        name: 'transaccion-listado-semanal',
                        component: TransaccionesSemanalesFormView,
                    },
                    {
                        path: 'mensual',
                        name: 'transaccion-listado-mensual',
                        component: TransaccionesMensualesFormView,
                    },
                    {
                        path: 'anual',
                        name: 'transaccion-listado-anual',
                        component: TransaccionesAnualesFormView,
                    },
                ]
            },
            {
                path: 'crear',
                name: 'transaccion-crear',
                component: TransaccionCrearView,
                redirect: { name: 'transaccion-crear-gasto' },
                meta: {
                    requiresAuth: true,
                },
                children: [
                    {
                        path: 'gasto',
                        name: 'transaccion-crear-gasto',
                        component: GastoCrearView,
                        meta: {
                            requiresAuth: true,
                            tipoTransaccion: "Gasto"
                        },
                    },
                    {
                        path: 'ingreso',
                        name: 'transaccion-crear-ingreso',
                        component: IngresoCrearView,
                        meta: {
                            requiresAuth: true,
                            tipoTransaccion: "Ingreso",
                        },
                    },
                    {
                        path: 'transferencia',
                        name: 'transaccion-crear-transferencia',
                        component: TransferenciaCrearView,
                        meta: {
                            requiresAuth: true,
                            tipoTransaccion: "Transferencia",
                        },
                    },
                ]
            },
        ]
    },
]