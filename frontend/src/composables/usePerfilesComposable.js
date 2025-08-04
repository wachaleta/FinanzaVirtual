import { usePerfilesStore } from "@/store/usePerfilesStore";
import { storeToRefs } from "pinia";

export const usePerfilesComposable = () => {
    const store = usePerfilesStore()

    const {
        perfil,
        perfiles,
        saldoTotalPerfiles,
    } = storeToRefs(store)
    
    const crearPerfil = async() => {
        await store.crearPerfil()
        await store.cargarPerfiles()
    }
    
    const editarPerfil = async() => {
        await store.editarPerfil()
        await store.cargarPerfiles()
        await store.obtenerSaldoTotalPerfiles()
    }
    
    const eliminarPerfil = async() => {
        await store.eliminarPerfil()
        await store.cargarPerfiles()
        await store.obtenerSaldoTotalPerfiles()
    }
    
    const cargarPerfiles = async() => await store.cargarPerfiles();
    const cargarPerfilPorId = async(idPerfil) => await store.cargarPerfilPorId(idPerfil);

    const obtenerSaldoTotalPerfiles = async() => await store.obtenerSaldoTotalPerfiles();

    return {
        perfil,
        saldoTotalPerfiles,
        perfiles,

        crearPerfil,
        editarPerfil,
        eliminarPerfil,
        cargarPerfiles,
        cargarPerfilPorId,
        obtenerSaldoTotalPerfiles,
    }
}