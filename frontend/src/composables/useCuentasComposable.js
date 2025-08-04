import { useCuentasStore } from "@/store/useCuentasStore";
import { storeToRefs } from "pinia";

export const useCuentasComposable = () => {
    const store = useCuentasStore()

    const {
        cuenta,
        cuentas,
    } = storeToRefs(store)

    const cargarCuentas = async() => store.cargarCuentas();

    return {
        cuenta,
        cuentas,

        cargarCuentas,
    }
}