import Api from "@/helpers/Api"

export default () => {
    let url = import.meta.env.VITE_API_BANCO_VIRTUAL
    return Api(url)
}