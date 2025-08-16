import { defineStore } from "pinia";
import { toast } from "vue3-toastify";
import router from '@/router'
import DebitoApi from "@/helpers/DebitoApi"

export const useCuentasStore = defineStore("cuentas", {
    state:() => {
        return{
            cuentas: [],
            cuenta: {},
        }
    },
    actions: {
        async crearCuenta() {
            await DebitoApi().post("cuenta/", this.cuenta)
            .then(() => {
                this.cuenta = {}
                toast.success("Cuenta Creada Exitosamente!")
            })
        },

        async editarCuenta() {
            await DebitoApi().put(`cuenta/${this.cuenta.IdCuenta}/`, this.cuenta)
            .then(() => {
                this.cuenta = {}

                router.push({name: 'cuenta-listado'}).then(() => {
                    toast.success("Cuenta Editada Exitosamente!")
                })
            })
        },

        async eliminarCuenta(idCuenta) {
            if(idCuenta){
                this.cuenta.IdCuenta = idCuenta
            }

            await DebitoApi().delete(`cuenta/${this.cuenta.IdCuenta}/`)
            .then(() => {
                
                router.push({name: 'cuenta-listado'}).then(() => {
                    toast.success(`Cuenta ${this.cuenta.Nombre} Eliminada Exitosamente!`)
                    this.cuenta = {}
                })
            })
        },

        async cargarCuentas(){
            await DebitoApi().get("cuenta")
            .then(res => {
                this.cuentas = res.data
            })
        },

        async cargarCuentaPorId(idCuenta){
            if(idCuenta){
                this.cuenta.IdCuenta = idCuenta
            }

            await DebitoApi().get(`cuenta/${this.cuenta.IdCuenta}`)
            .then(res => {
                this.cuenta = res.data
            })
        },
    }
})