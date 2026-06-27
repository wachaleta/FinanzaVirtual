import { useAuthStore } from "@/store/useAuthStore";
import { storeToRefs } from "pinia";
import { useRoute, useRouter } from "vue-router";

export const useAuthComposable = () => {
    const router = useRouter()
    const route = useRoute()
    const authStore = useAuthStore()

    const {
        credenciales
    } = storeToRefs(authStore)

    const iniciarSesion = async() => authStore.iniciarSesion();

    const registrarse = async() => authStore.registrarse();
    
    const cerrarSesion = async() => {
        localStorage.clear()
        router.push({name:'login', query: {nextUrl: route.name}})
    };

    return {
        credenciales,

        iniciarSesion,
        registrarse,
        cerrarSesion,
    }
}