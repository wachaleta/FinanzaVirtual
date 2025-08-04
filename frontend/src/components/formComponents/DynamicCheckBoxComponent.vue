<template>
    <div class="form-check form-switch pt-auto">
        <input class="form-check-input" v-model="model" type="checkbox" role="switch" :id="id">
        <label class="form-check-label" :for="id"><slot/></label>
    </div>
</template>

<script setup>

const model = defineModel()

defineProps({
    type: {
        type: String,
        default: "text"
    },
    
    id: {
        type: String,
        default: ""
    },
})
</script>