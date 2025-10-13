<template>
    <div>
        <ul>
            <slot>
            </slot>
        </ul>
        <RouterView/>
    </div>
</template>

<style scoped>
wul {
    list-style: none;
    display: flex;
    margin-bottom: 1.6rem;
    padding-left: 0;
}
</style>