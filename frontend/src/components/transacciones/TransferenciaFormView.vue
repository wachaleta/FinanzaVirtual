<template>
    <form @submit.prevent="$emit('submitForm')">
        <div class="row">
            <div class="col-6">
                <DynamicInputComponent type="number" min="1" v-model="model.monto" id="monto">
                    Monto
                </DynamicInputComponent>
            </div>
            <div class="col-6">
                <DynamicInputComponent type="date" v-model="model.fecha">Fecha:</DynamicInputComponent>
            </div>
        </div>
        <div class="row my-2">
            <!-- Ordenante -->
            <div class="col border">
                <div class="row">
                    <div class="col-1">
                        <p>De:</p>
                    </div>
                </div>
                <!-- Cuenta -->
                <div class="row">
                    <CuentaSelectComponent v-model="model.idCuentaOrdenante"/>
                </div>
                <!-- Perfil -->
                <div class="row">
                    <PerfilSelectComponent v-model="model.idPerfilOrdenante"/>
                </div>
            </div>
            <!-- Beneficiario -->
            <div class="col border ms-2">
                <div class="row">
                    <div class="col-1">
                        <p>Para:</p>
                    </div>
                </div>
                <!-- Cuenta -->
                <div class="row">
                    <CuentaSelectComponent v-model="model.idCuentaBeneficiaria"/>
                </div>
                <!-- Perfil -->
                <div class="row">
                    <PerfilSelectComponent v-model="model.idPerfilBeneficiario"/>
                </div>
            </div>
        </div>
        <!-- Categorias -->
        <div class="row">
            <div class="col-6">
                <CategoriaSelectComponent v-model="model.idCategoria" />
            </div>
            <div class="col-6">
                <DynamicInputComponent v-model="model.descripcion">Descripción</DynamicInputComponent>
            </div>
        </div>
        <div>
            <button type="submit" class="btn btn-success">Crear Transferencia</button>
        </div>
    </form>
</template>

<script setup>
import PerfilSelectComponent from '@/components/selectComponents/PerfilSelectComponent.vue';
import CuentaSelectComponent from '@/components/selectComponents/CuentaSelectComponent.vue';
import CategoriaSelectComponent from '@/components/selectComponents/CategoriaSelectComponent.vue';
import DynamicInputComponent from '@/components/formComponents/DynamicInputComponent.vue';

const model = defineModel()
</script>