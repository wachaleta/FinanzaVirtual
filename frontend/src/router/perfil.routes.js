import {
    PerfilListView,
    PerfilCrearView,
    PerfilEditarView,
} from '@/views/perfiles'

export default [
    {
        path: '/perfil', 
        name: 'perfil-listado',
        component: PerfilListView,
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
            },
            {
                path: 'crear', 
                name: 'perfil-crear',
                component: PerfilCrearView,
                meta: {
                },
            },
        ]
    },
]