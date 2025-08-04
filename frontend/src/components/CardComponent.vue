<template>
    <div :class="`card-container card-${color}`">
        <slot/>
    </div>
</template>

<script setup>


defineProps({
    color: {
        type: String,
        required: true
    }
})

</script>

<style>

.card-container {
    border-radius: 10px;
}

.card-success {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 1rem;
    background-color: #d4fde0;
    color:#259921
}

.card-danger {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 1rem;
    background-color: #f57979;
    color: #9c0d0d;
}

</style>