<template>
    <button class="align-middle" :class="`btn btn-${color}`" :type="type" @click="$emit('click')">
        <div class="row align-items-center">
            <div v-if="icon" class="col-2 pe-0" style="font-size: 0px;">
                <span class="material-symbols-outlined">
                    {{ icon }}
                </span>
            </div>
            <div class="col" style="font-size: 15px;">
                <slot />
            </div>
        </div>
    </button>
</template>

<script setup>

defineEmits(["click"])

defineProps({
    color: {
        type: String,
        default: "primary"
    },
    type: {
        type: String,
        default: "button"
    },
    icon: {
        type: String,
    },
})

</script>