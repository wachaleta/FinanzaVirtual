<template>
    <div class="container-component">
        <slot/>
    </div>
</template>

<style scoped>
.container-component {
    background-color: white;

    margin-left: 2rem;
    margin-right: 2rem;
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