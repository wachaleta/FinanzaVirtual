<template>
    <form 
        @submit.prevent="$emit('submitForm')" 
        class="row"
    >
        <div class="col-6">
            <DynamicInputComponent type="number" name="monto" min="1" v-model="model.monto" id="monto">
                Monto
            </DynamicInputComponent>
        </div>

        <div class="col-6">
            <DynamicInputComponent type="date" name="decha" v-model="model.fecha">Fecha:</DynamicInputComponent>
        </div>

        <div class="col-6">
            <CuentaSelectComponent v-model="model.idCuenta"/>
        </div>

        <div class="col-6">
            <PerfilSelectComponent v-model="model.idPerfil"/>
        </div>

        <div class="col-6">
            <CategoriaSelectComponent v-model="model.idCategoria"/>
        </div>

        <div class="col-6">
            <DynamicInputComponent v-model="model.descripcion" name="descripcion">Descripción</DynamicInputComponent>
        </div>

        <div>
            <button type="submit" class="btn btn-success">Crear {{ tipoTransaccion }}</button>
        </div>
    </form>
</template>

<script setup>

import {
    DynamicInputComponent
} from '@/components/inputComponents'

import {
    PerfilSelectComponent,
    CuentaSelectComponent,
    CategoriaSelectComponent,
} from '@/components/selectComponents'

const model = defineModel()
const emit = defineEmits(["submitForm"])

defineProps({
    tipoTransaccion: {
        type: String,
        required: true
    }
})

</script>