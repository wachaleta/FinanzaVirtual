import { usePerfilesStore } from "@/store/usePerfilesStore";
import { storeToRefs } from "pinia";

import { useErrorsComposable } from "./useErrorsComposable";

export const usePerfilesComposable = () => {
    const store = usePerfilesStore()
    const errors = useErrorsComposable()

    const {
        perfil,
        perfiles,
        saldosPerfiles,
    } = storeToRefs(store)
    
    const crearPerfil = async() => {
        await store.crearPerfil()
        errors.cleanErrors()
        await store.cargarPerfiles()
    }
    
    const editarPerfil = async() => {
        await store.editarPerfil()
        await store.cargarPerfiles()
        await store.obtenerSaldoTotalPerfiles()
    }
    
    const eliminarPerfil = async(IdPerfil) => {
        await store.eliminarPerfil(IdPerfil)
        await store.cargarPerfiles()
        await store.obtenerSaldoTotalPerfiles()
    }
    
    const cargarPerfiles = async() => await store.cargarPerfiles();
    const cargarPerfilPorId = async(idPerfil) => await store.cargarPerfilPorId(idPerfil);

    const obtenerSaldoTotalPerfiles = async() => await store.obtenerSaldoTotalPerfiles();

    return {
        perfil,
        saldosPerfiles,
        perfiles,

        crearPerfil,
        editarPerfil,
        eliminarPerfil,
        cargarPerfiles,
        cargarPerfilPorId,
        obtenerSaldoTotalPerfiles,
    }
}