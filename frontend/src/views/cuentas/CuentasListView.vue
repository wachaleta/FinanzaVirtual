<template>
    <RouterView/>
    <div class="row">
        <div class="col-7">
            <div class="ms-3">
                <h3>Cuentas</h3>
                <h6>Lugares donde se puede almacenar dinero</h6>
            </div>
        </div>
        <div class="col-5 text-end">
            <ButtonCrearComponent @click="router.push({name: 'cuenta-crear'})" class="mt-4"> Crear Cuenta </ButtonCrearComponent>
        </div>
    </div>

    <form @submit.prevent="cargarCuentas()">
        <div class="d-flex gap-3 px-3 mb-4 align-items-end">
            <div style="width: 10rem;">
                <ButtonBuscarComponent type="submit"/>
            </div>
            <div class="w-100">
                <DynamicInputComponent v-model="cuentasFiltros.searchText" name="searchText"/>
            </div>
        </div>
    </form>

    <div class="row">
        <div v-for="cuenta in cuentas" class="col-12 col-sm-6 col-md-4 mt-3">
            <CardComponent @click="router.push({name: 'cuenta-editar', params: {idCuenta: cuenta.id}})" :color="cuenta.saldo_total == cuenta.saldo_real_calculado? 'success':'danger'" class="h-100">
                <template v-slot:header>
                    {{ cuenta.nombre }}
                </template>

                <template v-slot:body>
                    <div>
                        Balance:
                    </div>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(cuenta.saldo_total) }}</strong>
                    </div>
                    <div v-if="cuenta.saldo_total != cuenta.saldo_real_calculado">
                        <strong >Diff({{ $filters.currencyGTQ(cuenta.saldo_real_calculado - cuenta.saldo_total) }})</strong>
                    </div>
                </template>
            </CardComponent>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

import { useCuentasComposable } from '@/composables/useCuentasComposable';
import { ButtonCrearComponent } from '@/components/buttonComponents'

import CardComponent from '@/components/CardComponent.vue';
import { useEfectivoMonedaComposable } from '@/composables/useEfectivoMonedaComposable';
import ButtonBuscarComponent from '@/components/buttonComponents/ButtonBuscarComponent.vue';
import DynamicInputComponent from '@/components/inputComponents/DynamicInputComponent.vue';

const router = useRouter()

const {
    cuentas,
    cuentasFiltros,

    cargarCuentas
} = useCuentasComposable()

const {
    cargarEfectivoMoneda,
} = useEfectivoMonedaComposable()

const refresh = async() => {
    cargarEfectivoMoneda()

    cuentasFiltros.value = {
        activo: true
    }
    await cargarCuentas()
}

refresh()

</script>