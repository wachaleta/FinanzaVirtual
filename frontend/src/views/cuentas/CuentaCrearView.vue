<template>
    <RouterView 
        @onAceptar="router.push({name: 'cuenta-listado'})"
        @onCancelar="router.push({name: 'cuenta-crear'})"
    />
    <form @submit.prevent="crearCuenta">
        <DynamicModalComponent size="sm"
            @onCancelar="router.push({name: 'cuenta-crear-cancelar'})">
            <template v-slot:header>
                Crear Cuenta
            </template>
            <template v-slot:body>
                <CuentaFormView>

                </CuentaFormView>
            </template>
        </DynamicModalComponent>
    </form>
</template>

<script setup>

import { useRouter } from 'vue-router'
import { useCuentasComposable } from '@/composables/useCuentasComposable';

import CuentaFormView from './CuentaFormView.vue';

import DynamicModalComponent from '@/components/DynamicModalComponent.vue';

const router = useRouter()

const {
    cuenta,
    
    crearCuenta,
} = useCuentasComposable()

const refresh = async() => {
    cuenta.value = {}
}

refresh()

</script>
