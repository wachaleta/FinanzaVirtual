<template>
    <RouterView 
        @onAceptar="router.push({name: 'categoria-listado'})"
        />
        <!-- @onCancelar="router.push({name: 'categoria-crear'})" -->
    <form @submit.prevent="editarCategoria">
        <DynamicModalComponent size="sm" :showDeleteButton="true"
        @onEliminar="router.push({name: 'categoria-eliminar'})"
            @onCancelar="router.push({name: 'categoria-editar-cancelar'})">
            <template v-slot:header>
                Editar Categoria {{ nombre }}
            </template>
            <template v-slot:body>
                <CategoriaFormView/>
            </template>
        </DynamicModalComponent>
    </form>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useErrorsComposable } from '@/composables/useErrorsComposable';
import { useCategoriasComposable } from '@/composables/useCategoriasComposable';

import CategoriaFormView from './CategoriaFormView.vue';
import DynamicModalComponent from '@/components/DynamicModalComponent.vue';

const router = useRouter()
const route = useRoute()

const nombre = ref("")

const xd = () => {
    alert("xe")
}
const {
    categoria,

    editarCategoria,
    cargarCategoriaPorId,
} = useCategoriasComposable()

const keyupHandler = (e) => {
    console.log(e.key)
    if(e.key == "Escape" && route.name == "categoria-editar")
    {
        router.push({name: 'categoria-editar-cancelar'})
        e.stopImmediatePropagation()
        document.activeElement.blur()
    }
}

onMounted(() => {
    window.addEventListener("keyup", keyupHandler)
})

onUnmounted(() => {
    window.removeEventListener("keyup", keyupHandler)
})

const refresh = async() => {
    await cargarCategoriaPorId(route.params.idCategoria)
    nombre.value = categoria.value.Nombre
}

refresh()

</script>
