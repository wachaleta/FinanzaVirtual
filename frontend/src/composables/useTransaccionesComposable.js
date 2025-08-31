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
        const EstablecerRango = transaccionesFiltros.value.EstablecerRango ?? false

        const fechaInicial = transaccionesFiltros.value.FechaInicialDiaria
        const fechaFinal = EstablecerRango? transaccionesFiltros.value.FechaFinalDiaria : fechaInicial
        
        if(EstablecerRango == true && fechaFinal != null || EstablecerRango == false)
            await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    const cargarTransaccionesSemanales = async() => {
        const EstablecerRango = transaccionesFiltros.value.EstablecerRango ?? false

        const fechaInicial = filters.getDateFromWeek(transaccionesFiltros.value.FechaInicialSemanal)
        const fechaFinal = EstablecerRango? filters.addDaysToDate(filters.getDateFromWeek(transaccionesFiltros.value.FechaFinalSemanal), 6) : filters.addDaysToDate(fechaInicial, 6)

        if(EstablecerRango == true && fechaFinal != null || EstablecerRango == false)
            await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    const cargarTransaccionesMensuales = async() => {
        const EstablecerRango = transaccionesFiltros.value.EstablecerRango ?? false

        const fechaInicial = filters.formatDate(transaccionesFiltros.value.FechaInicialMensual)

        const fechaFinal = EstablecerRango ?
            filters.ultimoDiaMes(transaccionesFiltros.value.FechaFinalMensual) 
            : filters.ultimoDiaMes(fechaInicial)
        

        if(EstablecerRango == true && fechaFinal != null || EstablecerRango == false)
            await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    const cargarTransaccionesAnuales = async() => {
        const EstablecerRango = transaccionesFiltros.value.EstablecerRango ?? false

        const fechaInicial = filters.primerDiaAnio(transaccionesFiltros.value.FechaInicialAnual)

        const fechaFinal = EstablecerRango ?
            filters.ultimoDiaAnio(transaccionesFiltros.value.FechaFinalAnual) 
            : filters.ultimoDiaAnio(fechaInicial)
        

        if(EstablecerRango == true && fechaFinal != null || EstablecerRango == false)
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
        cargarTransaccionesAnuales,
    }
}