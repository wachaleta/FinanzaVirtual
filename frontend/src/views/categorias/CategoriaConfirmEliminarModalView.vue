<template>
    <DynamicModalComponent style="z-index: 99999;"
        size="xs"
        okLabel="Sí, eliminar"
        @onAceptar="eliminarCategoria"
        @onCancelar="router.push({name: 'categoria-editar'})"
    >
        <template v-slot:header>
            Eliminar Categoria
        </template>

        <template v-slot:body>
            Seguro que desea eliminar la categoría <strong>{{ categoria.Nombre }}</strong>?
        </template>
    </DynamicModalComponent>
</template>

<script setup>

import { useRouter } from 'vue-router';
import { useCategoriasComposable } from '@/composables/useCategoriasComposable';

import DynamicModalComponent from '@/components/DynamicModalComponent.vue';
import { onMounted } from 'vue';

const router = useRouter()

onMounted(() => {
    document.activeElement.blur()
})

const {
    categoria,
    eliminarCategoria,
} = useCategoriasComposable()

</script>