const formatCurrencyGTQ = new Intl.NumberFormat('es-GT', { style: 'currency', currency: 'GTQ' })

export default {
    currencyGTQ(value) {
        if (value == null) {
            return '-'
        }
        return formatCurrencyGTQ.format(value)
    },
}