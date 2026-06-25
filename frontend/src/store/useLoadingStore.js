import { defineStore } from "pinia";

export const useLoadingStore = defineStore("loading", {
    state:() => {
        return{
            loads: 0,
            show: true
        }
    },
    actions: {
        validarShow(){
            if(this.loads <= 0){
                this.loads = 0;
                this.show = false;
            } else {
                this.show = true
            }
        },

        addLoad(){
            this.loads += 1
            this.validarShow()
        },

        deleteLoad(){
            this.loads -= 1
            this.validarShow()
        },
    }
})