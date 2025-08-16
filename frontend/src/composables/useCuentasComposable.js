import { useCuentasStore } from "@/store/useCuentasStore";
import { storeToRefs } from "pinia";

export const useCuentasComposable = () => {
    const store = useCuentasStore()

    const {
        cuenta,
        cuentas,
    } = storeToRefs(store)

    const crearCuenta = async() => {
        await store.crearCuenta()
        await store.cargarCuentas()
    }

    const editarCuenta = async() => {
        await store.editarCuenta()
        await store.cargarCuentas()
    }

    const eliminarCuenta = async(idCuenta) => {
        await store.eliminarCuenta(idCuenta)
        await store.cargarCuentas()
    }

    const cargarCuentas = async() => await store.cargarCuentas();
    const cargarCuentaPorId = async(idCuenta) => await store.cargarCuentaPorId(idCuenta);

    return {
        cuenta,
        cuentas,
        
        crearCuenta,
        editarCuenta,
        eliminarCuenta,
        cargarCuentas,
        cargarCuentaPorId,
    }
}