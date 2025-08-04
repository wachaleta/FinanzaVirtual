<template>
    <div class="mb-3">
        <label :for="id"
            :class="getErrors? 'error-label': ''"
        >
            <slot/>
        </label>
        <input 
            class="form-control"
            :class="getErrors? 'error': ''"
            v-model="model"
            :type="type"
            :id="id"
        >
        <div v-if="getErrors">
            <div v-for="error in getErrors" class="row">
                <label class="error-label">{{ error }}</label>
            </div>
        </div>
    </div>
</template>

<script setup>

import { useErrorsComposable } from '@/composables/useErrorsComposable';

const model = defineModel()

const props = defineProps({
    type: {
        type: String,
        default: "text"
    },

    name: {
        type: String,
        required: true
    },
    
    id: {
        type: String,
        default: ""
    },
})

const {
    getErrors,
} = useErrorsComposable(props.name)

</script>

<style scoped>

.error {
    border-color: rgb(255, 116, 116);
    border-width: 2px;
}

.error-label {
    height: 1rem;
    font-size: 0.9rem;
    color: red;
}
</style>