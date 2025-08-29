<template>
    <div class="form-check form-switch pt-auto">
        <input class="form-check-input" v-model="model" type="checkbox" role="switch" :id="name" @change="$emit('onChange')">
        <label class="form-check-label" :for="name"><slot/></label>
    </div>
</template>

<script setup>

const model = defineModel()

defineEmits(['onChange'])

defineProps({
    type: {
        type: String,
        default: "text"
    },
    name: {
        type: String,
        required: true
    },
})
</script>