import { useCategoriasStore } from "@/store/useCategoriasStore";
import { storeToRefs } from "pinia";

export const useCategoriasComposable = () => {
    const store = useCategoriasStore()

    const {
        categoria,
        categorias,
    } = storeToRefs(store)

    const cargarCategorias = async() => store.cargarCategorias();

    return {
        categoria,
        categorias,

        cargarCategorias,
    }
}