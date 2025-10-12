import {
    PerfilesListView,
    PerfilCrearView,
    PerfilEditarView,
    PerfilConfirmCancelarEditarModalView,
    ConfirmEliminarPerfilModalView,
} from '@/views/perfiles'

import ConfirmModalComponent from '@/components/ConfirmModalComponent.vue'

export default [
    {
        path: '/perfil', 
        name: 'perfil-listado',
        component: PerfilesListView,
        meta: {
            requiresAuth: true,
        },
        children: [
            {
                path: ':idPerfil/editar', 
                name: 'perfil-editar',
                component: PerfilEditarView,
                meta: {
                },
                children: [
                    {
                        path: 'cancelar', 
                        name: 'perfil-editar-cancelar',
                        component: PerfilConfirmCancelarEditarModalView,
                        meta: {
                        },
                    },
                    {
                        path: 'eliminar', 
                        name: 'perfil-editar-eliminar',
                        component: ConfirmEliminarPerfilModalView,
                        params: {
                        },
                        meta: {
                            title: `Eliminar Perfil`,
                            subtitle: "Seguro que desea eliminar el perfil?"
                        },
                    },
                ]
            },
            {
                path: 'crear', 
                name: 'perfil-crear',
                component: PerfilCrearView,
                meta: {
                },
                children:[
                    {
                        path: 'cancelar',
                        name: 'perfil-crear-cancelar',
                        component: ConfirmModalComponent,
                    }
                ]
            },
        ]
    },
]