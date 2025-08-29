<template>
    <div class="row">
        <div class="col-12">
            <DynamicInputComponent v-model="model.Nombre" name="Nombre">Nombre</DynamicInputComponent>
        </div>
        <div class="col-12">
            <DynamicCheckBoxComponent v-model="model.AgregarTotal" name="sumarTotalEditar">Sumar al disponible</DynamicCheckBoxComponent>
        </div>
    </div>
</template>

<script setup>
import { DynamicInputComponent } from '@/components/inputComponents'

import DynamicCheckBoxComponent from '@/components/formComponents/DynamicCheckBoxComponent.vue';

const model = defineModel()

</script>