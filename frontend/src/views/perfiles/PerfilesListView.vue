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
            <CardComponent :color="saldosPerfiles.SaldoTotal >= 0 ? 'success' : 'danger'" class="h-100">
                <template v-slot:header>
                    Saldo total
                </template>
                <template v-slot:body>
                    <div>
                        Balance:
                    </div>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(saldosPerfiles.SaldoTotal) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>

        <div class="col-12 col-sm-6 col-md-4 mt-3">
            <CardComponent :color="saldosPerfiles.SaldoSuma >= 0 ? 'success' : 'danger'" class="h-100">
                <template v-slot:header>
                    Saldo disponible
                </template>
                <template v-slot:body>
                    <div class="">
                        Balance:
                    </div>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(saldosPerfiles.SaldoSuma) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>

        <div class="col-12 col-sm-6 col-md-4 mt-3">
            <CardComponent :color="saldosPerfiles.SaldoNoSuma >= 0 ? 'success' : 'danger'" class="h-100">
                <template v-slot:header>
                    Saldo no disponible
                </template>
                <template v-slot:body>
                    <div class="">
                        Balance:
                    </div>
                    <div class="mt-2" style="font-size: 1.7rem;">
                        <strong>{{ $filters.currencyGTQ(saldosPerfiles.SaldoNoSuma) }}</strong>
                    </div>
                </template>
            </CardComponent>
        </div>
    </div>

    <div class="col-12 mt-5">
        <div class="ms-4">
            <h3>Perfiles con saldo disponible</h3>
            <h6>(Todo perfil con saldo negativo sumará al total)</h6>
        </div>

        <div class="row mt-4">
            <div class="col-12 col-sm-6 col-md-4" v-for="perfil in perfiles.filter(v => v.AgregarTotal == true || v.Saldo < 0)">
                <CardComponent @click="router.push({name: 'perfil-editar', params:{idPerfil: perfil.IdPerfil}})"
                class="mb-3"
                :color="perfil.Saldo >= 0 ? 'success' : 'danger'"
                >
                    <template v-slot:header>
                        {{ perfil.Nombre }}
                    </template>
                    <template v-slot:body>
                        <div class="">
                            Balance:
                        </div>
                        <div class="mt-2" style="font-size: 1.7rem;">
                            <strong>{{ $filters.currencyGTQ(perfil.Saldo) }}</strong>
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
            <div class="col-12 col-sm-6 col-md-4" v-for="perfil in perfiles.filter(v => v.AgregarTotal == false && v.Saldo >= 0)">
                <CardComponent @click="router.push({name: 'perfil-editar', params:{idPerfil: perfil.IdPerfil}})"
                class="mb-3"
                :color="perfil.Saldo >= 0 ? 'success' : 'danger'"
                >
                    <template v-slot:header>
                        {{ perfil.Nombre }}
                    </template>
                    <template v-slot:body>
                        <div class="">
                            Balance:
                        </div>
                        <div class="mt-2" style="font-size: 1.7rem;">
                            <strong>{{ $filters.currencyGTQ(perfil.Saldo) }}</strong>
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

const router = useRouter()

const {
    perfiles,
    saldosPerfiles,

    cargarPerfiles,
    obtenerSaldoTotalPerfiles,
} = usePerfilesComposable()

const refresh = async() => {
    await cargarPerfiles()
    await obtenerSaldoTotalPerfiles()
}

refresh()
</script>