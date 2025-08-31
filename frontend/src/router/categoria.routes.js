import ConfirmModalComponent from '@/components/ConfirmModalComponent.vue'

import {
    CategoriasListView,
    
    CategoriaCrearView,
    CategoriaConfirmCancelarCrearModalView,

    CategoriaEditarView,
    CategoriaConfirmCancelarEditarModalView,

    CategoriaConfirmEliminarModalView
} from '@/views/categorias'

export default [
    {
        path: '/categoria',
        name: 'categoria-listado',
        component: CategoriasListView,
        children: [
            {
                path: 'crear',
                name: 'categoria-crear',
                component: CategoriaCrearView,
                children:[
                    {
                        path: 'cancelar',
                        name: 'categoria-crear-cancelar',
                        component: CategoriaConfirmCancelarCrearModalView,
                    }
                ]
            },
            
            {
                path: 'editar/:idCategoria',
                name: 'categoria-editar',
                component: CategoriaEditarView,
                children:[
                    {
                        path: 'cancelar',
                        name: 'categoria-editar-cancelar',
                        component: CategoriaConfirmCancelarEditarModalView,
                    },
                    {
                        path: 'eliminar',
                        name: 'categoria-eliminar',
                        component: CategoriaConfirmEliminarModalView,
                    },
                ]
            },
        ]
    }
]