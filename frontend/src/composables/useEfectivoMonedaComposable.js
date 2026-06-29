import { useEfectivoMonedaStore } from "@/store/useEfectivoMonedaStore";
import { storeToRefs } from "pinia";

export const useEfectivoMonedaComposable = () => {
    const store = useEfectivoMonedaStore()

    const {
        efectivoMonedaFiltros,
        efectivoMonedaList,
    } = storeToRefs(store)

    const cargarEfectivoMoneda = () => store.cargarEfectivoMoneda()

    return {
        efectivoMonedaFiltros,
        efectivoMonedaList,

        cargarEfectivoMoneda,
    }
}