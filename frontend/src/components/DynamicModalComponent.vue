<template>
    <div class="hs-overlay">
        <div class="modal-wrapper">
            <div class="modal-container" :class="dynamicSize(size)">
                <div class="modal-header ms-1">
                    <h4 class="modal-title mt-3">
                        <strong>
                            <slot name="header"/>
                        </strong>
                    </h4>
                </div>
                <hr>
                <div class="modal-body">
                    <slot name="body"/>
                </div>
                <hr>
                <div class="modal-footer">
                    <slot name="footer">
                        <DynamicButtonComponent v-if="showDeleteButton" @click="$emit('onEliminar')" color="danger" class="me-2">Eliminar</DynamicButtonComponent>
                        <DynamicButtonComponent @click="$emit('onCancelar')" color="danger">Cancelar</DynamicButtonComponent>
                        <DynamicButtonComponent @click="$emit('onAceptar')" type="submit" class="ms-2">{{ okLabel }}</DynamicButtonComponent>
                    </slot>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import { DynamicButtonComponent } from '@/components/buttonComponents';

defineEmits(['onAceptar', 'onCancelar', 'onEliminar'])
const props = defineProps({
    size: {
        type: String,
        default: "lg"
    },
    okLabel: {
        type: String,
        default: "Guardar"
    },

    showDeleteButton: {
        type: Boolean,
        default: false
    }
})

const dynamicSize = (size) => {
    switch (size)
    {
        case "xs":
            return "modal-size-extra-small"

        case "sm":
            return "modal-size-small"

        case "md":
            return "modal-size-medium"

        case "lg":
            return "modal-size-large"
        
        case "xl":
            return "modal-size-extra-large"
    }
}   

</script>

<style scoped>
@keyframes modalIn{
    from {opacity: 0}
    to {opacity: 1}
}

.hs-overlay {
    display: inline;
    align-items: center;
    justify-content: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 9999;
    overflow-x: hidden;
    overflow-y: auto;
    background-color: rgba(0, 0, 0, 0.6);
    animation-name: modalIn;
    animation-duration: 0.2s;
}

.modal-wrapper {
    transition: margin-top 0.5s ease-out, opacity 0.5s ease-out;
    margin-top: 2rem;
    opacity: 1  ;
}

.modal-body {
    padding-left: 5%;
    padding-right: 5%;
}

.modal-container {
    position: relative;
    background: white;
    border-radius: 1rem;
    padding-left: 1rem;
    padding-right: 1rem;
    padding-bottom: 1rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    margin: auto;
    /* Añadir margen automático */
    left: 0;
    /* Añadir para centrar horizontalmente */
    right: 0;
    /* Añadir para centrar horizontalmente */
}

/* Tamaños del modal */

.modal-size-extra-small {
    max-width: 23%;
}

.modal-size-small {
    max-width: 30%;
}

.modal-size-medium {
    max-width: 50%;
}

.modal-size-large {
    max-width: 70%;
}

.modal-size-extra-large {
    max-width: 95%;
}

.modal-content {
    text-align: left;
    overflow-y: auto;
}

</style>
