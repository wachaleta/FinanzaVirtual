import { useTransaccionesStore } from "@/store/useTransaccionesStore";
import { storeToRefs } from "pinia";
import { useRoute } from 'vue-router'
import filters from "@/filters";

export const useTransaccionesComposable = () => {

const route = useRoute()
    const store = useTransaccionesStore()

    const {
        transaccion,
        transacciones,
        transaccionesFiltros,
    } = storeToRefs(store)

    const crearGasto = async() => await store.crearGasto()
    const crearIngreso = async() => await store.crearIngreso()
    const crearTransferencia = async() => await store.crearTransferencia()


    const cargarTransaccionesDiarias = async() => {
        const fechaInicial = transaccionesFiltros.value.FechaInicialDiaria
        const fechaFinal = transaccionesFiltros.value.EstablecerRango? transaccionesFiltros.value.FechaFinalDiaria : fechaInicial

        await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    const cargarTransaccionesSemanales = async() => {
        console.log(filters.semanaActual())
        
        const fechaInicial = filters.getDateFromWeek(transaccionesFiltros.value.FechaInicialSemanal)
        const fechaFinal = transaccionesFiltros.value.EstablecerRango? filters.addDaysToDate(filters.getDateFromWeek(transaccionesFiltros.value.FechaFinalSemanal), 6) : filters.addDaysToDate(fechaInicial, 6)

        await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    const cargarTransaccionesMensuales = async() => {
        const fechaInicial = filters.formatDate(transaccionesFiltros.value.FechaInicialMensual)

        const fechaFinal = transaccionesFiltros.value.EstablecerRango ?
            filters.ultimoDiaMes(transaccionesFiltros.value.FechaFinalMensual) 
            : filters.ultimoDiaMes(fechaInicial)

        await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    return {
        transaccion,
        transacciones,
        transaccionesFiltros,

        crearGasto,
        crearIngreso,
        crearTransferencia,

        cargarTransaccionesDiarias,
        cargarTransaccionesSemanales,
        cargarTransaccionesMensuales,
    }
}