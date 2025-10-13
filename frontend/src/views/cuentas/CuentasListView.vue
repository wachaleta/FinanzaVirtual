<template>
    <RouterView/>
    <div class="row">
        <div class="col-7">
            <div class="ms-3">
                <h3>Cuentas</h3>
                <h6>Lugares donde se puedan almacenar dinero</h6>
            </div>
        </div>
        <div class="col-5 text-end">
            <ButtonCrearComponent @click="router.push({name: 'cuenta-crear'})" class="mt-4"> Crear Cuenta </ButtonCrearComponent>
        </div>
    </div>

    <div class="row">
        <div v-for="cuenta in cuentas" class="col-12 col-sm-6 col-md-4 mt-3">
            <CardComponent @click="router.push({name: 'cuenta-editar', params: {idCuenta: cuenta.IdCuenta}})" :color="cuenta.SaldoTotal == cuenta.SaldoCalculado? 'success':'danger'">
                <template v-slot:header>
                    {{ cuenta.Nombre }}
                </template>

                <template v-slot:body>
                    <div>
                        Balance:
                    </div>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(cuenta.SaldoTotal) }}</strong>
                    </div>
                    <div v-if="cuenta.SaldoTotal != cuenta.SaldoCalculado">
                        <strong >Diff({{ $filters.currencyGTQ(cuenta.SaldoCalculado - cuenta.SaldoTotal) }})</strong>
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

const router = useRouter()

const {
    cuentas,

    cargarCuentas
} = useCuentasComposable()

const refresh = async() => {
    await cargarCuentas()
}

refresh()

</script>