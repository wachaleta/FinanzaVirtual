<template>
    <RouterView/>
    <ContainerComponent class="mt-3">
        <div class="row m-0 px-3 mt-2">
            <div class="col-12 col-md-6">
                <h3>Saldo total: Q{{ saldoTotalPerfiles }}</h3>
            </div>
            <div class="col-12 col-md-6 text-end">
                <DynamicButtonComponent @click="router.push({name: 'perfil-crear'})" color="primary"> Crear Perfil </DynamicButtonComponent>
            </div>
        </div>
    </ContainerComponent>
        <div class="row m-0 p-3">
            <div class="col-12 mb-3">
                <div class="row">
                    <h4>Perfiles que suman al saldo total</h4>
                </div>
                <div class="row d-flex justify-content-center">
                    <ContainerComponent v-for="perfil in perfiles.filter(v => v.AgregarTotal)" @click="router.push({name: 'perfil-editar', params:{idPerfil: perfil.IdPerfil}})"
                        class="col-3 m-2 p-3"
                        >
                        <h5 class="ms-2">{{ perfil.Nombre }}</h5>
                        <CardComponent
                            class="mt-3"
                            :color="perfil.Saldo >= 0 ? 'success' : 'danger'"
                        >
                            <div class="">
                                Balance:
                            </div>
                            <div class="mt-2" style="font-size: 1.7rem;">
                                <strong>Q{{ perfil.Saldo }}</strong>
                            </div>
                        </CardComponent>
                    </ContainerComponent>
                </div>
            </div>
        </div>
    <ContainerComponent>
        <div class="row m-0 p-3">
            <div class="col-12">
                <div class="row">
                    <h5>Perfiles que no suman al saldo total</h5>
                </div>
                <div class="row d-flex justify-content-center">
                    <CardComponent v-for="perfil in perfiles.filter(v => !v.AgregarTotal)" @click="router.push({name: 'perfil-editar', params:{idPerfil: perfil.IdPerfil}})"
                        class="col-3 m-2 p-3"
                        :color="perfil.Saldo >= 0 ? 'success' : 'danger'"
                    >
                        <div class="row m-0">
                            <div class="col-6">
                                Nombre:
                            </div>
                            <div class="col-6 text-end">
                                {{ perfil.Nombre }}
                            </div>
                        </div>
                        <div class="row m-0">
                            <div class="col-6">
                                Saldo:
                            </div>
                            <div class="col-6 text-end">
                                Q{{ perfil.Saldo }}
                            </div>
                        </div>
                    </CardComponent>
                </div>
            </div>
        </div>
    </ContainerComponent>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { usePerfilesComposable } from '@/composables/usePerfilesComposable';

import ContainerComponent from '@/components/ContainerComponent.vue';
import DynamicButtonComponent from '@/components/formComponents/DynamicButtonComponent.vue';
import CardComponent from '@/components/CardComponent.vue';

const router = useRouter()

const {
    perfiles,
    saldoTotalPerfiles,

    cargarPerfiles,
    obtenerSaldoTotalPerfiles,
} = usePerfilesComposable()

const refresh = async() => {
    await cargarPerfiles()
    await obtenerSaldoTotalPerfiles()
}

refresh()
</script>