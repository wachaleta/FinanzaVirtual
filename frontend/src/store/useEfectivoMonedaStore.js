import { defineStore } from "pinia";
import CatalogosApi from "@/helpers/CatalogosApi";
import { toast } from 'vue3-toastify'

export const useEfectivoMonedaStore = defineStore("efectivo-moneda", {
    state:() => {
        return{
            efectivoMonedaFiltros: {},
            efectivoMonedaList: [],
        }
    },
    actions: {
        async cargarEfectivoMoneda(){
            await CatalogosApi().get("efectivo-moneda/",
                {
                    params: this.efectivoMonedaFiltros
                }
            )
            .then(res => {
                this.efectivoMonedaList = res.data
            })
        },

    }
})