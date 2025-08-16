import {
    CuentasListView,
    CuentaCrearView,
    CuentaEditarView,
    CuentaConfirmEliminarModalView,
    CuentaConfirmCancelarEditarModalView,
} from '@/views/cuentas'

import ConfirmModalComponent from '@/components/ConfirmModalComponent.vue'

export default [
    {
        path: '/cuenta', 
        name: 'cuenta-listado',
        component: CuentasListView,
        meta: {
            requiresAuth: true,
        },
        children: [
            {
                path: 'crear', 
                name: 'cuenta-crear',
                component: CuentaCrearView,
                meta: {
                },
                children: [
                    {
                        path: 'cancelar', 
                        name: 'cuenta-crear-cancelar',
                        component: ConfirmModalComponent,
                    },
                ]
            },
            {
                path: 'editar/:idCuenta', 
                name: 'cuenta-editar',
                component: CuentaEditarView,
                meta: {
                },
                children: [
                    {
                        path: 'cancelar', 
                        name: 'cuenta-editar-cancelar',
                        component: CuentaConfirmCancelarEditarModalView,
                        children: [
                        ]
                    },
                    {
                        path: 'eliminar', 
                        name: 'cuenta-editar-eliminar',
                        component: CuentaConfirmEliminarModalView,
                        children: [
                        ]
                    },
                ]
            },
        ]
    },
]