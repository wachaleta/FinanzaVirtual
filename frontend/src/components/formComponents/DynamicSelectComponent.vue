<template>
    <div class="mb-3">
        <label :for="id">
            <slot/>
        </label>
        <select :name="name" :id="id" v-model="model" class="form-select">
            <option v-for="item in items" :value="item[valueRef]">{{ optionText(item) }}</option>
        </select>
    </div>
</template>

<script setup>

// import vSelect from 'vue-select'

defineProps({
    name: String,
    id: String,
    
    valueRef: {
        type: String,
        required: true,
    },

    optionText: {
        type: Function,
        required: true,
    },

    items: {
        type: Object,
        required: true
    },
})

const model = defineModel()

</script>