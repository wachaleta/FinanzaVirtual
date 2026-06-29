import { defineStore } from "pinia";
import { toast } from "vue3-toastify";
import router from '@/router'
import DebitoApi from "@/helpers/DebitoApi"

export const useCuentasStore = defineStore("cuentas", {
    state:() => {
        return{
            cuentas: [],
            cuentasFiltros: {},
            cuentaEfectivo: {},
            cuenta: {},
        }
    },
    actions: {
        async crearCuenta() {
            this.cuenta.efectivo = {...this.cuentaEfectivo}

            await DebitoApi().post("cuenta/", this.cuenta)
            .then(() => {
                this.cuenta = {}
                toast.success("Cuenta Creada Exitosamente!")
            })
        },

        async editarCuenta() {
            this.cuenta.efectivo = {...this.cuentaEfectivo}
            await DebitoApi().put(`cuenta/${this.cuenta.id}/`, this.cuenta)
            .then(() => {
                this.cuenta = {}

                router.push({name: 'cuenta-listado'}).then(() => {
                    toast.success("Cuenta Editada Exitosamente!")
                })
            })
        },

        async eliminarCuenta(idCuenta) {
            if(idCuenta){
                this.cuenta.id = idCuenta
            }

            await DebitoApi().put(`cuenta/${this.cuenta.id}/inactivar/`)
            .then(() => {
                
                router.push({name: 'cuenta-listado'}).then(() => {
                    toast.success(`Cuenta ${this.cuenta.nombre} Eliminada Exitosamente!`)
                    this.cuenta = {}
                })
            })
        },

        async cargarCuentas(){
            await DebitoApi().get("cuenta/",
                {
                    params: this.cuentasFiltros
                }
            )
            .then(res => {
                this.cuentas = res.data
            })
        },

        async cargarCuentaPorId(idCuenta){
            if(idCuenta){
                this.cuenta.id = idCuenta
            }

            await DebitoApi().get(`cuenta/${this.cuenta.id}/`)
            .then(res => {
                this.cuenta = res.data

                for(const clave in this.cuenta.cuentaefectivo_set){
                    const item = this.cuenta.cuentaefectivo_set[clave]
                    this.cuentaEfectivo[item.efectivo_moneda] = item.cantidad_efectivo
                }
            })
        },
    }
})