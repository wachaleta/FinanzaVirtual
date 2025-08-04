<template>
    <div class="row">
        <div class="col-12">
            <DynamicInputComponent v-model="model.Nombre" name="Nombre">Nombre</DynamicInputComponent>
        </div>
        <div class="col-12">
            <DynamicCheckBoxComponent v-model="model.AgregarTotal" id="sumarTotalEditar">Sumar al saldo total</DynamicCheckBoxComponent>
        </div>
    </div>
</template>

<script setup>
import DynamicInputComponent from '@/components/formComponents/DynamicInputComponent.vue';
import DynamicCheckBoxComponent from '@/components/formComponents/DynamicCheckBoxComponent.vue';

const model = defineModel()

</script>