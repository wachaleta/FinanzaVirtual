import dayjs from 'dayjs'
import weekOfYear from "dayjs/plugin/weekOfYear";
// var weekOfYear = require("dayjs/plugin/weekOfYear");
const formatCurrencyGTQ = new Intl.NumberFormat('es-GT', { style: 'currency', currency: 'GTQ' })
dayjs.extend(weekOfYear);

export default {
    currencyGTQ(value) {
        if (!value) {
            return '-'
        }
        return formatCurrencyGTQ.format(value)
    },

    getDateFromWeek(fecha){
        if(!fecha){
            return null
        }

        let fechas = fecha.split("-")

        let newDate = new dayjs(fechas[0]).startOf('week')
        const semanas = fechas[1].substring(1)
        newDate = newDate.add(semanas - 1, 'week')
        newDate = newDate.add(1, 'day')

        return this.formatDate(newDate)
    },

    addDaysToDate(fecha, dias = 1){
        if(fecha == null){
            return null
        }

        const newDate = new dayjs(fecha)

        return this.formatDate(newDate.add(dias, 'day'))
    },

    addMonthsToDate(fecha, meses = 1){
        if(fecha == null){
            return null
        }
        const newDate = new dayjs(fecha)
        
        return this.formatDate(newDate.add(meses, 'month'))
    },

    formatDate(fecha, formato="YYYY-MM-DD"){
        if(fecha == null)
        {
            return null
        }
        const newFecha = new dayjs(fecha)

        return newFecha.format(formato)
    },
    fechaActual(formato="YYYY-MM-DD"){
        let hoy = new dayjs()

        hoy = this.formatDate(hoy, formato)
        return hoy
    },

    semanaActual(){
        // var weekOfYear = require("dayjs/plugin/weekOfYear");


        const semana = dayjs().week(); 
        console.log("semana")
        const semanaFormateada = dayjs().year() + "-W" + dayjs().week()
        console.log(semanaFormateada)
        return semanaFormateada
    },

    ultimoDiaMes(fecha){
        const newDate  = this.formatDate(dayjs(fecha).endOf('month'))

        return newDate
    },

    primerDiaMes(fecha){
        const newDate  = this.formatDate(dayjs(fecha).startOf('month'))

        return newDate
    },
}