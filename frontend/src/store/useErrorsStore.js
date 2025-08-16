import { defineStore } from "pinia";
import AuthApi from "@/helpers/AuthApi";
import router from "@/router/";

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