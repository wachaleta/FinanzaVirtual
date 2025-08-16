<template>
    <!-- @onAceptar="router.push({name: 'cuenta-listado'})"
    @onCancelar="router.push({name: 'cuenta-editar'})" -->
    <RouterView 
    />
    <form @submit.prevent="editarCuenta">
        <DynamicModalComponent size="sm" :showDeleteButton="true"
            @onCancelar="router.push({name: 'cuenta-editar-cancelar'})"
            @onEliminar="router.push({name: 'cuenta-editar-eliminar'})"
        >
            <template v-slot:header>
                Editar {{ nombre }}
            </template>
            <template v-slot:body>
                <CuentaFormView/>
            </template>
        </DynamicModalComponent>
    </form>
</template>

<script setup>

import { useRoute, useRouter } from 'vue-router'
import { useCuentasComposable } from '@/composables/useCuentasComposable';

import CuentaFormView from './CuentaFormView.vue';

import DynamicModalComponent from '@/components/DynamicModalComponent.vue';
import { ref } from 'vue';

const nombre = ref("")
const route = useRoute()
const router = useRouter()

const {
    cuenta,

    editarCuenta,
    cargarCuentaPorId,
} = useCuentasComposable()

const refresh = async() => {
    cuenta.value = {}
    await cargarCuentaPorId(route.params.idCuenta)
    nombre.value = cuenta.value.nombre
}

refresh()

</script>
