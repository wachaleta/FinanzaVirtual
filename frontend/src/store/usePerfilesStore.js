import { defineStore } from "pinia";
import BancoVirtualApi from "@/helpers/BancoVirtualApi"
import DebitoApi from "@/helpers/DebitoApi";
import { toast } from 'vue3-toastify'

export const usePerfilesStore = defineStore("perfiles", {
    state:() => {
        return{
            perfiles: [],
            perfil: {},
            saldoTotalPerfiles: 0,
        }
    },
    actions: {
        async crearPerfil() {
            await DebitoApi().post("perfil-crear", this.perfil)
            .then(() => {
                this.perfil = {}
                toast.success("Perfil Creado Exitosamente!")
            })
        },

        async editarPerfil() {
            await DebitoApi().put(`perfil/${this.perfil.IdPerfil}/editar`, this.perfil
            )
            .then(() => {
                this.perfil= {}
                toast.success("Perfil Editado Exitosamente!")
            })
        },

        async eliminarPerfil(IdPerfil) {
            if(IdPerfil)
            {
                this.perfil.IdPerfil = IdPerfil
            }

            await DebitoApi().delete(`perfil/${this.perfil.IdPerfil}/eliminar`
            )
            .then(() => {
                this.perfil= {}
                toast.success("Perfil Eliminado Exitosamente!")
            })
        },

        async cargarPerfiles(){
            await BancoVirtualApi().get("perfil")
            .then(res => {
                this.perfiles = res.data
            })
        },

        async cargarPerfilPorId(IdPerfil){
            await BancoVirtualApi().get(`perfil/${IdPerfil}`)
            .then(res => {
                this.perfil = res.data
            })
        },

        async obtenerSaldoTotalPerfiles(){
            await BancoVirtualApi().get("total-saldo-perfiles")
            .then(res => {
                this.saldoTotalPerfiles = res.data.Saldo
            })
        },
    }
})