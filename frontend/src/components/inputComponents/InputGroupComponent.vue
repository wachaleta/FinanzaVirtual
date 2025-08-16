<template>
    <div>
        <div class="input-group">
            <label class="input-group-text" :class="getErrors? 'input-error': ''" :for="name">
                <slot/>
            </label>
            <input
                :id="name"
                :type="type"
                class="form-control"
                :class="getErrors? 'error': ''"
                v-model="model"
            >
        </div>
        <div v-if="getErrors" class="mb-3">
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
        required: true,
    },
})

const {
    getErrors,
} = useErrorsComposable(props.name)

</script>