<template>
  <form @submit.prevent="iniciarSesion()">
    <div class="row h-100vh justify-content-center pb-5 align-items-center">
      <div class="col-12 col-lg-6">
        <CardComponent class="pb-4">
          <template #body>
            <div class="row justify-content-center">
              <div class="col-9">
                <h3 class="text-center text-title">Iniciar Sesión</h3>
                <div class="mb-3">
                  <DynamicInputComponent v-model="credenciales.username" name="username" placeholder="Nombre de Usuario">
                    Usuario
                  </DynamicInputComponent>
                </div>
                <div class="mb-3">
                  <DynamicInputComponent v-model="credenciales.password" name="password" type="password" placeholder="Ingrese la Contraseña">
                    Contraseña
                  </DynamicInputComponent>
                </div>
                <div class="text-center help-text">
                  <p>
                    No tienes una cuenta? <RouterLink :to="{name: 'register'}"> Crear una </RouterLink>
                  </p>
                </div>
              </div>
              <!-- <button type="submit" class="btn btn-light"><i class="bx bxs-lock-open"></i>Iniciar Sesión</button> -->
              <div class="text-end me-3">
                <DynamicButtonComponent type="submit" color="secondary">
                  Iniciar Sesión
                </DynamicButtonComponent>
              </div>
            </div>
          </template>
        </CardComponent>
      </div>
    </div>
  </form>
</template>

<script setup>
import { useRouter } from 'vue-router';

import { useAuthComposable } from '@/composables/useAuthComposable';

import { DynamicButtonComponent } from '../buttonComponents';

import CardComponent from '../CardComponent.vue';
import DynamicInputComponent from '../inputComponents/DynamicInputComponent.vue';

const router = useRouter()

const {
  credenciales,

  iniciarSesion,
} = useAuthComposable()

const refresh = async () => {
  credenciales.value = {}
}

refresh()

const irRegister = () => {
  router.push({name: 'register'})
}

</script>