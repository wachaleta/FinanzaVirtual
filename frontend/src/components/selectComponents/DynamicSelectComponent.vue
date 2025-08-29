<template>
    <div class="mb-3">
        <label :for="name" :class="{ 'error-label': getErrors }">
            <slot />
        </label>
        <multiselect v-model="objeto" :id="name" :class="{ 'input-error': getErrors }" select-label="Seleccionar"
            selected-label="Seleccionado" deselect-label="Deseleccionar" :track-by="valueRef"
            :close-on-select="closeOnSelect" :multiple="multiple" :placeholder="placeholder" :custom-label="optionText"
            :options="items" @select="onSeleccionar" @remove="onRemover">

        </multiselect>
        <div v-if="getErrors">
            <div v-for="error in getErrors" class="row">
                <label class="error-label">{{ error }}</label>
            </div>
        </div>
    </div>
</template>

<script setup>
import Multiselect from 'vue-multiselect'

import { useErrorsComposable } from '@/composables/useErrorsComposable';
import { ref, watch } from 'vue';

const emits = defineEmits(['onSelect', 'onRemove'])

const props = defineProps({
    name: String,

    valueRef: {
        type: String,
        required: true,
    },

    multiple: {
        type: Boolean,
        default: false
    },

    closeOnSelect: {
        type: Boolean,
        default: true
    },

    placeholder: {
        type: String,
        default: "Seleccione una opción",
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
const objeto = defineModel("objeto")

const {
    getErrors,
} = useErrorsComposable(props.name)


const onSeleccionar = (selectedOption, id) => {
    if (props.multiple == true) {
        model.value = objeto.value.map(v => v[props.valueRef])
    } else {
        model.value = selectedOption[props.valueRef]
    }

    emits('onSelect')
}

const onRemover = (removedOption, id) => {
    if (props.multiple == true) {
        model.value = objeto.value.map(v => v[props.valueRef])
    } else {
        model.value = null
    }

    emits('onRemove')
}

const refresh = () => {
    if (props.multiple == false) {
        objeto.value = props.items.find(v => v[props.valueRef] == model.value)
    } else {
        if (model.value != null) {
            objeto.value = props.items.filter(v => model.value.includes(v[props.valueRef]))
        }
    }
}
refresh()

watch(model, refresh)

</script>