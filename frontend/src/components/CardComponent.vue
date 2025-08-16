<template>
    <div class="container px-3">
        <h5 class="ms-2">
            <strong>
                <slot name="header" class="header"/>
            </strong>
        </h5>
        <div :class="`card-container card-${color}`">
            <slot name="body"/>
        </div>
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

.container {
    padding-top: 1rem;
    padding-bottom: 1rem;

    background-color: white;
    border-radius: 1rem;
    box-shadow: 0px 7px 8px rgba(138, 138, 138, 0.438);
}

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