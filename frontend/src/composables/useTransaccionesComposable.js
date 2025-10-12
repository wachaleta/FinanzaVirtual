import { useTransaccionesStore } from "@/store/useTransaccionesStore";
import { storeToRefs } from "pinia";
import { useRoute, useRouter } from 'vue-router'
import { toast } from 'vue3-toastify'
import filters from "@/filters";

export const useTransaccionesComposable = () => {

    const route = useRoute()
    const router = useRouter()
    const store = useTransaccionesStore()

    const {
        transaccion,
        transacciones,
        transaccionesFiltros,
    } = storeToRefs(store)

    //  POST
    const crearGasto = async () => await store.crearGasto()
    const crearIngreso = async () => await store.crearIngreso()
    const crearTransferencia = async () => await store.crearTransferencia()

    //  PUT
    const editarGasto = async () => {
        await store.editarGasto()
            .then(() => {
                const next = route.query.next ?? 'transaccion-listado'
                router.push({ name: next }).then(() => {
                    toast.success("Gasto Editado Exitosamente!")
                })
            })
    }

    const editarIngreso = async () => {
        await store.editarIngreso()
            .then(() => {
                const next = route.query.next ?? 'transaccion-listado'
                router.push({ name: next }).then(() => {
                    toast.success("Ingreso Editado Exitosamente!")
                })
            })
    }

    const editarTransferencia = async () => {
        await store.editarTransferencia()
            .then(() => {
                const next = route.query.next ?? 'transaccion-listado'
                router.push({ name: next }).then(() => {
                    toast.success("Transferencia Editada Exitosamente!")
                })
            })
    }

    //  GET
    const cargarTransaccionPorId = async (idTransaccion) => await store.cargarTransaccionPorId(idTransaccion)

    const cargarTransaccionesDiarias = async () => {
        const EstablecerRango = transaccionesFiltros.value.EstablecerRango ?? false

        const fechaInicial = transaccionesFiltros.value.FechaInicialDiaria
        const fechaFinal = EstablecerRango ? transaccionesFiltros.value.FechaFinalDiaria : fechaInicial

        if (EstablecerRango == true && fechaFinal != null || EstablecerRango == false)
            await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    const cargarTransaccionesSemanales = async () => {
        const EstablecerRango = transaccionesFiltros.value.EstablecerRango ?? false

        const fechaInicial = filters.getDateFromWeek(transaccionesFiltros.value.FechaInicialSemanal)
        const fechaFinal = EstablecerRango ? filters.addDaysToDate(filters.getDateFromWeek(transaccionesFiltros.value.FechaFinalSemanal), 6) : filters.addDaysToDate(fechaInicial, 6)

        if (EstablecerRango == true && fechaFinal != null || EstablecerRango == false)
            await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    const cargarTransaccionesMensuales = async () => {
        const EstablecerRango = transaccionesFiltros.value.EstablecerRango ?? false

        const fechaInicial = filters.formatDate(transaccionesFiltros.value.FechaInicialMensual)

        const fechaFinal = EstablecerRango ?
            filters.ultimoDiaMes(transaccionesFiltros.value.FechaFinalMensual)
            : filters.ultimoDiaMes(fechaInicial)


        if (EstablecerRango == true && fechaFinal != null || EstablecerRango == false)
            await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    const cargarTransaccionesAnuales = async () => {
        const EstablecerRango = transaccionesFiltros.value.EstablecerRango ?? false

        const fechaInicial = filters.primerDiaAnio(transaccionesFiltros.value.FechaInicialAnual)

        const fechaFinal = EstablecerRango ?
            filters.ultimoDiaAnio(transaccionesFiltros.value.FechaFinalAnual)
            : filters.ultimoDiaAnio(fechaInicial)


        if (EstablecerRango == true && fechaFinal != null || EstablecerRango == false)
            await store.cargarTransacciones(fechaInicial, fechaFinal)
    }

    //  DELETE
    const eliminarTransaccion = async () => {
        await store.eliminarTransaccion()
            .then(() => {
                const next = route.query.next ?? 'transaccion-listado'
                router.push({ name: next }).then(() => {
                    toast.success("Transacción Eliminada Exitosamente!")
                })
            })
    }

    return {
        transaccion,
        transacciones,
        transaccionesFiltros,

        crearGasto,
        crearIngreso,
        crearTransferencia,

        editarGasto,
        editarIngreso,
        editarTransferencia,

        cargarTransaccionPorId,
        cargarTransaccionesDiarias,
        cargarTransaccionesSemanales,
        cargarTransaccionesMensuales,
        cargarTransaccionesAnuales,

        eliminarTransaccion,
    }
}