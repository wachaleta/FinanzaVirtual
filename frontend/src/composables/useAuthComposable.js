import { useAuthStore } from "@/store/useAuthStore";
import { storeToRefs } from "pinia";

export const useAuthComposable = () => {
    const authStore = useAuthStore()

    const {
        credenciales
    } = storeToRefs(authStore)

    const iniciarSesion = async() => authStore.iniciarSesion();

    return {
        credenciales,

        iniciarSesion
    }
}