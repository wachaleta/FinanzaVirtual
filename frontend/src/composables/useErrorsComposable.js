import { useErrorsStore } from "@/store/useErrorsStore";
import { storeToRefs } from "pinia";
import { computed } from "vue";

export const useErrorsComposable = (name='') => {
    const errorsStore = useErrorsStore()

    const {
        errors
    } = storeToRefs(errorsStore)

    const getErrors = computed(() => {

        if(errors.value)
        {
            const key = Object.keys(errors.value).find(v => v.toLowerCase() == name.toLowerCase())
            return errors.value[key]
        }
    })

    const setErrors = (data) => errorsStore.setErrors(data)

    const cleanErrors = () => errorsStore.cleanErrors()

    return {
        errors,

        getErrors,
        setErrors,
        cleanErrors,
    }
}