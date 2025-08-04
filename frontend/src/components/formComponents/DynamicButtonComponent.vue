<template>
    <button 
        :class="`btn btn-${color}`"
        :type="type"
        @click="$emit('click')"
    >
        <slot/>
    </button>
</template>

<script setup>

defineEmits(["click"])

defineProps({
    color:{
        type: String,
        default: "primary"
    },
    type:{
        type: String,
        default: "button"
    },
})

</script>