import { defineStore } from "pinia";
import { toast } from 'vue3-toastify'
import router from '@/router'

import DebitoApi from "@/helpers/DebitoApi"
export const useCategoriasStore = defineStore("categorias", {
    state:() => {
        return{
            categorias: [],
            categoria: {},
        }
    },
    actions: {
        async crearCategoria(){
            await DebitoApi().post("categoria/", this.categoria)
                .then(() => {
                    this.categoria = {}
                    toast.success("Categoría Creada Exitosamente!")
                })
        },

        async editarCategoria(){
            await DebitoApi().put(`categoria/${this.categoria.IdCategoria}/`, this.categoria)
                .then(() => {
                    router.push({name: 'categoria-listado'}).then(() => {
                        toast.success("Categoría Editada Exitosamente!")
                    })
                })
        },

        async eliminarCategoria(){
            await DebitoApi().put(`categoria/${this.categoria.IdCategoria}/inactivar/`)
                .then(() => {
                    router.push({name: 'categoria-listado'}).then(() => {
                        toast.success(`Categoría ${this.categoria.Nombre} Eliminada Exitosamente!`)
                    })
                })
        },

        async cargarCategorias(){
            await DebitoApi().get("categoria/")
            .then(res => {
                this.categorias = res.data
            })
        },

        async cargarCategoriaPorId(idCategoria){

            if(idCategoria){
                this.categoria.IdCategoria = idCategoria
            }

            await DebitoApi().get(`categoria/${this.categoria.IdCategoria}/`)
            .then(res => {
                this.categoria = res.data
            })
        },
    }
})