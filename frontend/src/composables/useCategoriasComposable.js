import { useCategoriasStore } from "@/store/useCategoriasStore";
import { storeToRefs } from "pinia";

export const useCategoriasComposable = () => {
    const store = useCategoriasStore()

    const {
        categoria,
        categorias,
    } = storeToRefs(store)

    const crearCategoria = async() => {
        await store.crearCategoria()
        store.cargarCategorias()
    };

    const editarCategoria = async() => {
        await store.editarCategoria()
        store.cargarCategorias()
    };

    const eliminarCategoria = async() => {
        await store.eliminarCategoria()
        store.cargarCategorias()
    };

    const cargarCategorias = async() => await store.cargarCategorias();
    const cargarCategoriaPorId = async(idCategoria) => await store.cargarCategoriaPorId(idCategoria);

    return {
        categoria,
        categorias,

        crearCategoria,
        editarCategoria,
        eliminarCategoria,
        
        cargarCategorias,
        cargarCategoriaPorId,
    }
}