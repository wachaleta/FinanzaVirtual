import { defineStore } from "pinia";
import { toast } from 'vue3-toastify'
import DebitoApi from "@/helpers/DebitoApi";
import filters from "@/filters";

export const useTransaccionesStore = defineStore("transacciones", {
    state: () => {
        return {
            transacciones: [],
            transaccionesFiltros: {
                FechaInicialDiaria: filters.fechaActual(),
                FechaInicialSemanal: filters.semanaActual(),
                FechaInicialMensual: filters.formatDate(filters.primerDiaMes(filters.fechaActual()), "YYYY-MM"),
                FechaInicialAnual: filters.formatDate(filters.fechaActual(), "YYYY"),
                FechaFinalAnual: filters.formatDate(filters.fechaActual(), "YYYY"),
            },
            transaccion: {
                fecha: filters.fechaActual()
            }
        }
    },
    actions: {
        //  POST
        async crearGasto() {
            await DebitoApi().post("gasto/", this.transaccion)
                .then(() => {
                    toast.success("Gasto Creado Exitosamente!")
                    const fecha = this.transaccion.fecha
                    this.transaccion = {}
                    this.transaccion.fecha = fecha
                })
        },

        async crearIngreso() {
            await DebitoApi().post("ingreso/", this.transaccion)
                .then(() => {
                    toast.success("Ingreso Creado Exitosamente!")
                    const fecha = this.transaccion.fecha
                    this.transaccion = {}
                    this.transaccion.fecha = fecha
                })
        },

        async crearTransferencia() {
            await DebitoApi().post("transferencia/", this.transaccion)
                .then(() => {
                    toast.success("Transferencia Creada Exitosamente!")
                    const fecha = this.transaccion.fecha
                    const transferencia_entre_perfiles = this.transaccion.transferencia_entre_perfiles
                    
                    this.transaccion = {}
                    this.transaccion.fecha = fecha
                    this.transaccion.transferencia_entre_perfiles = transferencia_entre_perfiles
                })
        },

        //  PUT
        async editarGasto() {
            await DebitoApi().put(`gasto/${this.transaccion.id}/`, this.transaccion)
        },

        async editarIngreso() {
            await DebitoApi().put(`ingreso/${this.transaccion.id}/`, this.transaccion)
        },

        async editarTransferencia() {
            await DebitoApi().put(`transferencia/${this.transaccion.id}/`, this.transaccion)
        },

        //  GET
        async cargarTransacciones(fechaInicial = null, fechaFinal = null) {
            const queryParams = {
                fechaInicial: fechaInicial,
                fechaFinal: fechaFinal,
            }
            const params = new URLSearchParams()

            for (const clave in queryParams) {
                if (queryParams[clave]) {
                    params.append(clave, queryParams[clave])
                }
            }

            for (const id in this.transaccionesFiltros.IdPerfiles) {
                params.append("IdPerfiles", this.transaccionesFiltros.IdPerfiles[id])
            }

            for (const id in this.transaccionesFiltros.IdCuentas) {
                params.append("IdCuentas", this.transaccionesFiltros.IdCuentas[id])
            }

            for (const id in this.transaccionesFiltros.IdCategorias) {
                params.append("IdCategorias", this.transaccionesFiltros.IdCategorias[id])
            }

            const querySearch = params.toString()
            await DebitoApi().get("transacciones-rango-fechas/?" + querySearch)
                .then(res => {
                    this.transacciones = res.data
                })
        },

        async cargarTransaccionPorId(idTransaccion) {

            if (idTransaccion) {
                this.transaccion.id = idTransaccion
            }

            await DebitoApi().get(`transaccion/${this.transaccion.id}/`)
                .then(res => {
                    this.transaccion = res.data
                })
        },

        //  DELETE
        async eliminarTransaccion() {
            await DebitoApi().delete(`transaccion/${this.transaccion.id}/`)
        },
    }
})