import { defineStore } from "pinia";
import BancoVirtualApi from "@/helpers/BancoVirtualApi"

export const useCuentasStore = defineStore("cuentas", {
    state:() => {
        return{
            cuentas: [],
            cuenta: {},
        }
    },
    actions: {
        async cargarCuentas(){
            await BancoVirtualApi().get("cuenta")
            .then(res => {
                this.cuentas = res.data
            })
        },
    }
})