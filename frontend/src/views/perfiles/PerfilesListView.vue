<template>
    <RouterView/>
    <div class="row">
        <div class="col-7">
            <div class="ms-3">
                <h3>Perfiles</h3>
                <h6>Entidades a quienes les pertenezca el dinero</h6>
            </div>
        </div>
        <div class="col-5 text-end">
            <ButtonCrearComponent @click="router.push({name: 'perfil-crear'})" class="mt-4"> Crear Perfil </ButtonCrearComponent>
        </div>
    </div>


    <!-- Cards para saldos -->
    <div class="row">
        <div class="col-12 col-sm-6 col-md-4 mt-3">
            <CardComponent :color="saldosPerfiles.saldo_total >= 0 ? 'success' : 'danger'" class="h-100">
                <template v-slot:header>
                    Saldo total
                </template>
                <template v-slot:body>
                    <div>
                        Balance:
                    </div>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(saldosPerfiles.saldo_total) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>

        <div class="col-12 col-sm-6 col-md-4 mt-3">
            <CardComponent :color="saldosPerfiles.SaldoDisponible >= 0 ? 'success' : 'danger'" class="h-100">
                <template v-slot:header>
                    Saldo disponible
                </template>
                <template v-slot:body>
                    <div class="">
                        Balance:
                    </div>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(saldosPerfiles.SaldoDisponible) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>

        <div class="col-12 col-sm-6 col-md-4 mt-3">
            <CardComponent :color="saldosPerfiles.SaldoNoDisponible >= 0 ? 'success' : 'danger'" class="h-100">
                <template v-slot:header>
                    Saldo no disponible
                </template>
                <template v-slot:body>
                    <div class="">
                        Balance:
                    </div>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(saldosPerfiles.SaldoNoDisponible) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>
    </div>

    <form @submit.prevent="cargarPerfiles()">
        <div class="d-flex gap-3 px-3 mt-4 align-items-end">
            <div style="width: 10rem;">
                <ButtonBuscarComponent type="submit"/>
            </div>
            <div class="w-100">
                <DynamicInputComponent v-model="perfilesFiltros.searchText" name="searchText"/>
            </div>
        </div>
    </form>

    <div class="col-12 mt-5">
        <div class="ms-4">
            <h3>Perfiles con saldo disponible</h3>
            <h6>(Todo perfil con saldo negativo sumará al total)</h6>
        </div>

        <div class="row mt-4">
            <div class="col-12 col-sm-6 col-md-4" v-for="perfil in perfiles.filter(v => v.suma_disponible == true || v.saldo < 0)">
                <CardComponent @click="router.push({name: 'perfil-editar', params:{idPerfil: perfil.id}})"
                class="mb-3"
                :color="perfil.saldo >= 0 ? 'success' : 'danger'"
                >
                    <template v-slot:header>
                        {{ perfil.nombre }}
                    </template>
                    <template v-slot:body>
                        <div class="">
                            Balance:
                        </div>
                        <div class="mt-2" style="font-size: 1.7rem;">
                            <strong>{{ $filters.currencyGTQ(perfil.saldo) }}</strong>
                        </div>
                    </template>
                </CardComponent>
            </div>
        </div>
    </div>

    <div class="col-12 mt-5">
        <div class="ms-4">
            <h3>Perfiles con saldo no disponible</h3>
        </div>

        <div class="row mt-4">
            <div class="col-12 col-sm-6 col-md-4" v-for="perfil in perfiles.filter(v => v.suma_disponible == false && v.saldo >= 0)">
                <CardComponent @click="router.push({name: 'perfil-editar', params:{idPerfil: perfil.id}})"
                class="mb-3"
                :color="perfil.saldo >= 0 ? 'success' : 'danger'"
                >
                    <template v-slot:header>
                        {{ perfil.nombre }}
                    </template>
                    <template v-slot:body>
                        <div class="">
                            Balance:
                        </div>
                        <div class="mt-2" style="font-size: 1.7rem;">
                            <strong>{{ $filters.currencyGTQ(perfil.saldo) }}</strong>
                        </div>
                    </template>
                </CardComponent>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import { ButtonCrearComponent } from '@/components/buttonComponents';
import CardComponent from '@/components/CardComponent.vue';
import DynamicInputComponent from '../../components/inputComponents/DynamicInputComponent.vue';
import DynamicButtonComponent from '../../components/buttonComponents/DynamicButtonComponent.vue';
import ButtonBuscarComponent from '../../components/buttonComponents/ButtonBuscarComponent.vue';

const router = useRouter()

const {
    perfiles,
    perfilesFiltros,
    saldosPerfiles,

    cargarPerfiles,
    obtenerSaldoTotalPerfiles,
} = usePerfilesComposable()

const refresh = async() => {
    perfilesFiltros.value = {
        activo: true
    }
    cargarPerfiles()
    obtenerSaldoTotalPerfiles()
}

refresh()
</script>