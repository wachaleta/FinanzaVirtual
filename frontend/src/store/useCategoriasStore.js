import { defineStore } from "pinia";
import BancoVirtualApi from "@/helpers/BancoVirtualApi"

export const useCategoriasStore = defineStore("categorias", {
    state:() => {
        return{
            categorias: [],
            categoria: {},
        }
    },
    actions: {
        async cargarCategorias(){
            await BancoVirtualApi().get("categoria")
            .then(res => {
                this.categorias = res.data
            })
        },
    }
})