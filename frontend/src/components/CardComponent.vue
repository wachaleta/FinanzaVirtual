<template>
    <div class="container px-3">
        <div class="row">
            <div class="col">
                <div class="row">

                    <h5 class="ms-2">
                        <strong>
                            <slot name="header" class="header" />
                        </strong>
                    </h5>
                    <div class="col">
                        <div v-if="$slots.descripcion" class="mb-3 ms-2">
                            <slot name="descripcion"></slot>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-4">

                <span class="fecha text-end">
                    <slot name="fecha">
                    </slot>
                </span>
            </div>
        </div>

        <div :class="`card-container card-${color}`">
            <slot name="body" />
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

.fecha {
    color: #787878;
    font-size: 0.87rem;
}

.card-container {
    border-radius: 10px;
}

.card-success {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 1rem;
    background-color: #d4fde0;
    color: #259921
}

.card-info {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 1rem;
    background-color: #bcedf8;
    color: #218399
}

.card-danger {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 1rem;
    background-color: #ffb7b7;
    color: #b44747;
}
</style>