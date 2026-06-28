import { defineStore } from "pinia";
import DebitoApi from "@/helpers/DebitoApi";
import { toast } from 'vue3-toastify'
import router from '@/router'

export const usePerfilesStore = defineStore("perfiles", {
    state:() => {
        return{
            perfiles: [],
            perfilesFiltros: {},
            perfil: {},
            saldosPerfiles: {
                SaldoTotal: 0,
                SaldoDisponible: 0,
                SaldoNoDisponible: 0,
            },
        }
    },
    actions: {
        async crearPerfil() {
            await DebitoApi().post("perfil/", this.perfil)
            .then(() => {
                this.perfil = {}
                toast.success("Perfil Creado Exitosamente!")
            })
        },

        async editarPerfil() {
            await DebitoApi().put(`perfil/${this.perfil.id}/`, this.perfil
            )
            .then(() => {
                this.perfil= {}
                
                router.push({name: 'perfil-listado'}).then(() => {
                    toast.success("Perfil Editado Exitosamente!")
                })
            })
        },

        async eliminarPerfil(idPerfil) {
            if(idPerfil)
            {
                this.perfil.id = idPerfil
            }

            await DebitoApi().put(`perfil/${this.perfil.id}/inactivar/`
            )
            .then(() => {
                router.push({name: 'perfil-listado'}).then(() => {
                    toast.success(`Perfil ${this.perfil.Nombre} Eliminado Exitosamente!`)
                    this.perfil= {}
                })
            })
        },

        async cargarPerfiles(){
            await DebitoApi().get("perfil/",
                {
                    params: this.perfilesFiltros
                }
            )
            .then(res => {
                this.perfiles = res.data
            })
        },

        async cargarPerfilPorId(idPerfil){
            await DebitoApi().get(`perfil/${idPerfil}/`)
            .then(res => {
                this.perfil = res.data
            })
        },

        async obtenerSaldoTotalPerfiles(){
            await DebitoApi().get("total-saldo-perfiles/")
            .then(res => {
                this.saldosPerfiles = res.data
            })
        },
    }
})