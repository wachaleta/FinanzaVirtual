import CrearTransaccion from '@/components/transacciones/CrearTransaccion.vue'
import GastoCrearView from '@/components/transacciones/GastoCrearView.vue'
import IngresoCrearView from '@/components/transacciones/IngresoCrearView.vue'
import TransferenciaCrearView from '@/components/transacciones/TransferenciaCrearView.vue'

export default [
    {path: '/', redirect: {name: 'transaccion-crear'}},
    {
        path: '/transaccion/crear', 
        name: 'transaccion-crear',
        component: CrearTransaccion,
        redirect: {name: 'transaccion-crear-gasto'},
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
                },
            },
            {
                path: 'ingreso', 
                name: 'transaccion-crear-ingreso',
                component: IngresoCrearView,
                meta: {
                    requiresAuth: true,
                },
            },
            {
                path: 'transferencia', 
                name: 'transaccion-crear-transferencia',
                component: TransferenciaCrearView,
                meta: {
                    requiresAuth: true,
                },
            },
        ]
    },
]