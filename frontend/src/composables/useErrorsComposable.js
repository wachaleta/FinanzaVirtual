import { useErrorsStore } from "@/store/useErrorsStore";
import { storeToRefs } from "pinia";
import { computed } from "vue";

export const useErrorsComposable = (name='') => {
    const errorsStore = useErrorsStore()

    const {
        errors
    } = storeToRefs(errorsStore)

    const getErrors = computed(() => {
        if(errors.value && errors.value.errores)
        {
            const key = Object.keys(errors.value.errores).find(v => v.toLowerCase() == name.toLowerCase())
            return errors.value.errores[key]
        }
    })

    const setErrors = errorsStore.setErrors()

    return {
        errors,

        getErrors,
        setErrors,
    }
}