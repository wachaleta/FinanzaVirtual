import { defineStore } from "pinia";
import AuthApi from "@/helpers/AuthApi";
import router from "@/router/";

export const useAuthStore = defineStore("auth", {
    state:() => {
        return{
            credenciales: {}
        }
    },
    actions: {
        async iniciarSesion(){
            console.log("logueando ando")
            await AuthApi().post("login2/", this.credenciales)
            .then(res => {
                console.log(res)
                localStorage.setItem("access", res.data.access)
                localStorage.setItem("refresh", res.data.refresh)

                router.push({name: 'transaccion-crear'} )
            })
            // .catch((e) => {
            //     toast.error(e)
            // })
        }
    }
})