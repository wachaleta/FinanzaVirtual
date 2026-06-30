import { toast } from 'vue3-toastify'
import { useErrorsComposable } from '@/composables/useErrorsComposable'
import axios from 'axios'
import router from '@/router'
import { useErrorsStore } from '@/store/useErrorsStore'
import { useLoadingStore } from '../store/useLoadingStore'


export default (baseURL = "") => {
    const errorsComposable = useErrorsStore()
    const loading = useLoadingStore()

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
            loading.addLoad()
            errorsComposable.cleanErrors()
            return request
        }
    )

    axiosInstance.interceptors.response.use(
        (response) => {
            loading.deleteLoad()
            return response
        },
        (error) => {
            loading.deleteLoad()
            errorsComposable.setErrors(error.response.data)

            if(error.response.data.code == 'token_not_valid')
            {
                localStorage.clear()
                router.push({name: "login"})
            }

            const data = error.response.data

            console.log("data")
            console.log(error.response)
            console.log(typeof(data))

            if(typeof(data) == 'object' && data != null && Object.values(data)[0]) {
                toast.error(Object.values(data)[0])
            } else {
                toast.error("Ha ocurrido un error inesperado")
            }
            return Promise.reject(error)
        }
    )

    return axiosInstance;
}