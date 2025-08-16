<template>
    <div class="container-component">
        <div class="container-body" :class="color">
            <slot/>
        </div>
    </div>
</template>

<script setup>
defineProps({
    color: {
        type: String,
        default: "white"
    }
})
</script>

<style scoped>
.white {
    background-color: white;
}

.darken-white {
  background-color: #f6f8fb;
    /* background-color: #d8e9fa; */
}

.container-component {
    padding-left: 2rem;
    padding-right: 2rem;
}

.container-body {
    /* margin-left: 2rem;
    margin-right: 2rem; */
    padding-left: 2rem;
    padding-right: 2rem;
    margin-bottom: 1.5rem;
    
    padding-top:      1rem;
    padding-bottom:   1rem;
    
    /* border-color: #b3b3b3; */
    /* border-style: solid; */
    border-radius: 1rem;
    /* border-width: 0.1rem; */
    
    box-shadow: 0px 7px 8px rgba(138, 138, 138, 0.438);
}
</style>