import Api from "@/helpers/Api"

export default () => {
    let url = import.meta.env.VITE_API_DEBITO
    return Api(url)
}