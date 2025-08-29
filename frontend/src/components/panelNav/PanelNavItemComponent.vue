<template>
    <RouterLink :to="{name: to}">
        <div class="panel-nav-item">
            <slot/>
        </div>
    </RouterLink>
</template>

<script setup>
defineProps({
    to: {
        type: String,
        required: true
    },
    color: {
        type: String,
        default: "white"
    }
})
</script>

<style scoped>

a {
    text-decoration: none;
}

.router-link-active > .panel-nav-item {
    background-color: rgb(1, 148, 227);
    color:white;
}

.panel-nav-item {
    background-color: white;
    color: black;
    padding-left: 2rem;
    padding-right: 2rem;
    
    padding-top:      1rem;
    padding-bottom:   1rem;
    
    border-radius: 1rem;
    
    box-shadow: 0px 7px 8px rgba(138, 138, 138, 0.438);
}
</style>