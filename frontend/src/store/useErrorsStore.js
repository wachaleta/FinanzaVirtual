import { defineStore } from "pinia";

export const useErrorsStore = defineStore("errors", {
    state:() => {
        return{
            errors: null
        }
    },
    actions: {
        setErrors(errors) {
            this.errors = errors
        },

        cleanErrors() {
            this.errors = {}
        },
    }
})