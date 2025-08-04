<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark" style="width: 100%; position: sticky; top: 0px; left: 0px; z-index: 100;">
    <div class="container-fluid">
        <a class="navbar-brand" href="/#" style="margin: 0; padding: 0;">
            <!-- <img src="/static/imagenes/logo.png" alt="Logo" style="width: 31px; translate: 0 -1px; margin: 0;"> -->
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <RouterLink class="nav-link active" :to="{name: 'perfil-listado'}" aria-current="page">Perfiles</RouterLink>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/cuentas">Cuentas</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" style="color: white;">
                    Transacciones
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li>
                            <RouterLink class="dropdown-item" :to="{name: 'transaccion-crear'}">Crear Transaccion</RouterLink>
                        </li>
                        <li>
                            <!-- <RouterLink class="dropdown-item" :to="{name: 'transaccion-listado'}">Ver Transacciones</RouterLink> -->
                        </li>
                        <li>
                            <a class="dropdown-item" href="/transaccion/programada">Transacciones Programadas</a>
                        </li>
                    </ul>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/categorias">Categorías</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/prueba">Prueba</a>
                </li>
            </ul>
            <div class="d-flex">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Nombre Usuario
                        </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li>
                            <a class="dropdown-item" href="#">Perfil</a>
                        </li>
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li>
                            <a class="dropdown-item" href="/logout">Cerrar Sesión</a>
                        </li>
                    </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</nav>
<!-- <div style="margin-bottom: 60px"></div> -->
</template>

<script setup>

import { RouterLink } from 'vue-router';

</script>