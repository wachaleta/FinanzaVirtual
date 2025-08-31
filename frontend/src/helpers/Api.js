import { toast } from 'vue3-toastify'
import { useErrorsComposable } from '@/composables/useErrorsComposable'
import axios from 'axios'
import router from '@/router'
import { useErrorsStore } from '@/store/useErrorsStore'


export default (baseURL = "") => {
    const errorsComposable = useErrorsStore()

    var headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    if(localStorage.getItem("access")){
        headers.Authorization = "Bearer " + localStorage.getItem('access');
    }

    const axiosInstance = axios.create({
        baseURL: baseURL,
        withCredentials: false,
        headers: headers,
    })

    axiosInstance.interceptors.request.use(
        (request) => {
            errorsComposable.cleanErrors()
            return request
        }
    )

    axiosInstance.interceptors.response.use(
        (response) => response,
        (error) => {
            console.log(error)
            
            errorsComposable.setErrors(error.response.data)

            if(error.response.data.code == 'token_not_valid')
            {
                localStorage.clear()
                router.push({name: "login"})
            }

            if(error.response.data.detail) {
                toast.error(error.response.data.detail)
            } else {
                toast.error("Ha ocurrido un error inesperado")
            }
            return Promise.reject(error)
        }
    )

    return axiosInstance;
}