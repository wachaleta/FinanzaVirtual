import { useTransaccionesStore } from "@/store/useTransaccionesStore";
import { storeToRefs } from "pinia";

export const useTransaccionesComposable = () => {
    const store = useTransaccionesStore()

    const {
        transaccion,
    } = storeToRefs(store)


    return {
        transaccion,
    }
}