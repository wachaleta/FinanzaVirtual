<template>
  <form @submit.prevent="iniciarSesion">
    <div class="col-12">
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
    </div>
  </form>
</template>

<script setup>
import { useAuthComposable } from '@/composables/useAuthComposable';

const {
  credenciales,

  iniciarSesion,
} = useAuthComposable()
</script>