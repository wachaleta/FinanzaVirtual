<template>
    <DynamicButtonComponent icon="search" color="secondary" class="btn-ssm" @click="$emit('click')">
        Buscar
    </DynamicButtonComponent>
</template>

<script setup>
import DynamicButtonComponent from './DynamicButtonComponent.vue';

defineEmits(["click"])

</script>