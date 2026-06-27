<template>
  <form @submit.prevent="registrarse()">
    <div class="row h-100vh justify-content-center pb-5 align-items-center">
      <div class="col-6">
        <CardComponent class="pb-4">
          <template #body>
            <div class="row justify-content-center">
              <div class="col-9">
                <h3 class="text-center text-title">Registrarse</h3>
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

                <div class="mb-3">
                  <DynamicInputComponent v-model="credenciales.password_again" name="password_again" type="password" placeholder="Ingrese la Contraseña de nuevo">
                    Repetir Contraseña
                  </DynamicInputComponent>
                </div>
              </div>
              <!-- <button type="submit" class="btn btn-light"><i class="bx bxs-lock-open"></i>Iniciar Sesión</button> -->
              <div class="text-end me-3">
                <DynamicButtonComponent class="me-3" color="info" @click="router.push({name: 'login'})">
                  Ya tienes una cuenta? Iniciar Sesión
                </DynamicButtonComponent>
                <DynamicButtonComponent type="submit" color="info">
                  Crear Cuenta
                </DynamicButtonComponent>
              </div>
            </div>
          </template>
        </CardComponent>
      </div>
    </div>
    <!-- <div class="col-12">
      <label for="inputEmailAddress" class="form-label">Usuario</label>
      <input type="text" v-model="credenciales.username" autofocus class="form-control" id="inputEmailAddress" placeholder="Nombre de Usuario">
    </div>
    <div class="col-12">
      <label for="inputChoosePassword" class="form-label">Contraseña</label>
      <div class="input-group" id="show_hide_password">
        <input type="password" v-model="credenciales.password" class="form-control border-end-0" id="inputChoosePassword" value="" placeholder="Ingrese la Contraseña"> <a href="javascript:;" class="input-group-text bg-transparent"><i class='bx bx-hide'></i></a>
      </div>
    </div>
    <div class="col-md-4">
      <div class="form-check form-switch">
        <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked>
        <label class="form-check-label" for="flexSwitchCheckChecked">Recuérdame</label>
      </div>
    </div>
    <div class="col-md-8 text-end">	<a href="authentication-forgot-password.html">¿Olvidaste tu Contraseña?</a>
    </div>
    <div class="col-12">
      <div class="d-grid">
        <button type="submit" class="btn btn-light"><i class="bx bxs-lock-open"></i>Iniciar Sesión</button>
        <hr/>
      </div>
    </div> -->
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

  registrarse,
} = useAuthComposable()

const refresh = async () => {
  credenciales.value = {}
}

refresh()

</script>