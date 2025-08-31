<template>
    <div class="mb-3">
        <label :for="name"
            :class="{'error-label': getErrors}"
        >
            <slot/>
        </label>
        <input 
            class="form-control"
            :ref="ref"
            :class="{error: getErrors}"
            v-model="model"
            :type="type"
            :step="step"
            :min="min"
            :id="name"
            @change="$emit('onChange')"
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

defineEmits(['onChange'])

const props = defineProps({
    type: {
        type: String,
        default: "text"
    },

    step: {
        type: String,
        default: "1"
    },

    ref: {
        type: String,
    },

    min: {
        type: String
    },

    name: {
        type: String,
        required: true
    },
})

const {
    getErrors,
} = useErrorsComposable(props.name)

</script>