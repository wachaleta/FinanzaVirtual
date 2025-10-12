import {
    TransaccionesListView,
    TransaccionesDiariasFormView,
    TransaccionesSemanalesFormView,
    TransaccionesMensualesFormView,
    TransaccionesAnualesFormView,

    TransaccionCrearView,
    TransaccionEditarView,
    TransaccionEliminarModalView,

    GastoCrearView,
    GastoEditarView,

    IngresoCrearView,
    IngresoEditarView,

    TransferenciaCrearView,
    TransferenciaEditarView,
} from '@/views/transacciones'

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
                redirect: { name: 'transaccion-listado-diario' },
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
                ]
            },
            {
                path: 'transferencia/crear',
                name: 'transaccion-crear-transferencia',
                component: TransferenciaCrearView,
                meta: {
                    requiresAuth: true,
                    tipoTransaccion: "Transferencia",
                },
            },
            {
                path: ':idTransaccion/editar',
                name: 'transaccion-editar',
                component: TransaccionEditarView,
                redirect: { name: 'gasto-editar' },
                children: [
                    {
                        path: 'gasto',
                        name: 'gasto-editar',
                        component: GastoEditarView,
                        meta: {
                            keepQuery: true,
                            tipoTransaccion: "Gasto"
                        },
                        children: [
                            {
                                path: 'eliminar',
                                name: 'gasto-eliminar',
                                component: TransaccionEliminarModalView,
                                meta: {
                                    keepQuery: true,
                                    tipoTransaccion: "Gasto"
                                },
                            },
                        ]
                    },
                    {
                        path: 'ingreso',
                        name: 'ingreso-editar',
                        component: IngresoEditarView,
                        meta: {
                            keepQuery: true,
                            tipoTransaccion: "Ingreso"
                        },
                        children: [
                            {
                                path: 'eliminar',
                                name: 'ingreso-eliminar',
                                component: TransaccionEliminarModalView,
                                meta: {
                                    keepQuery: true,
                                    title: 'Eliminar Ingreso',
                                    subtitle: '¿Seguro que deseas eliminar el ingreso?',
                                    tipoTransaccion: "Ingreso"
                                },
                            },
                        ]
                    },
                ]
            },
            {
                path: 'transferencia/:idTransaccion/editar',
                name: 'transferencia-editar',
                component: TransferenciaEditarView,
                meta: {
                    keepQuery: true
                },
                children: [
                    {
                        path: 'eliminar',
                        name: 'transferencia-eliminar',
                        component: TransaccionEliminarModalView,
                        meta: {
                            keepQuery: true,
                            title: "Eliminar Transferencia",
                            subtitle: '¿Seguro que deseas eliminar la transferencia?'
                        },
                    },
                ]
            },
        ]
    },
]