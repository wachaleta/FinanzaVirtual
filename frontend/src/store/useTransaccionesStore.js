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
                Fecha: filters.fechaActual()
            }
        }
    },
    actions: {
        async crearGasto() {
            await DebitoApi().post("gasto/", this.transaccion)
                .then(() => {
                    toast.success("Gasto Creado Exitosamente!")
                    const fecha = this.transaccion.Fecha
                    this.transaccion = {}
                    this.transaccion.Fecha = fecha
                })
        },

        async crearIngreso() {
            await DebitoApi().post("ingreso/", this.transaccion)
                .then(() => {
                    toast.success("Ingreso Creada Exitosamente!")
                    const fecha = this.transaccion.Fecha
                    this.transaccion = {}
                    this.transaccion.Fecha = fecha
                })
        },

        async crearTransferencia() {
            await DebitoApi().post("transferencia/", this.transaccion)
                .then(() => {
                    toast.success("Transferencia Creada Exitosamente!")
                    const fecha = this.transaccion.Fecha
                    this.transaccion = {}
                    this.transaccion.Fecha = fecha
                })
        },

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

            for(const id in this.transaccionesFiltros.IdPerfiles){
                params.append("IdPerfiles", this.transaccionesFiltros.IdPerfiles[id])
            }

            for(const id in this.transaccionesFiltros.IdCuentas){
                params.append("IdCuentas", this.transaccionesFiltros.IdCuentas[id])
            }

            for(const id in this.transaccionesFiltros.IdCategorias){
                params.append("IdCategorias", this.transaccionesFiltros.IdCategorias[id])
            }

            const querySearch = params.toString()
            await DebitoApi().get("transaccion?" + querySearch)
                .then(res => {
                    this.transacciones = res.data
                })
        }
    }
})