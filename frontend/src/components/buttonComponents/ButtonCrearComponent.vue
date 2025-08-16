<template>
    <DynamicButtonComponent icon="new_window" color="success" @click="$emit('click')">
        <slot>
            Crear
        </slot>
    </DynamicButtonComponent>
</template>

<script setup>
import DynamicButtonComponent from './DynamicButtonComponent.vue';

defineEmits(["click"])

</script>