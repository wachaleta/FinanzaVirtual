<template>
    <!-- Botones de selección de transacción -->
    <div class="row d-flex justify-content-evenly xd">
        <!-- Botón de gasto -->
        <div class="col-1">
            <button type="button" class="btn btn-success" @click="router.push({name: 'transaccion-crear-gasto'})">Gasto</button>
        </div>
        <!-- Botón de ingreso -->
        <div class="col-1">
            <button type="button" @click="router.push({name: 'transaccion-crear-ingreso'})" class="btn btn-success">Ingreso</button>
        </div>
        <!-- Botón de transferencia -->
        <div class="col-1">
            <button type="button" @click="router.push({name: 'transaccion-crear-transferencia'})" class="btn btn-success">Transferencia</button>
        </div>
    </div>
    <div class="row d-flex justify-content-center">
        <div class="col-11 p-5" id="container" style="margin-top: 13px;">
            <!-- Formulario para gastos e ingresos -->
            <div class="form-control m-3">
                <div class="row d-flex align-content-center mb-2">
                    <router-view/>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const hoy =(fecha = new Date()) => {
    let formato = "yyyy-MM-dd"
    let dia = fecha.getDate()
    dia = (dia < 10)? "0" + dia : dia;
    let mes = fecha.getMonth() + 1;
    mes = (mes < 10)? "0" + mes : mes;

    let nueva_fecha = formato.replace("yyyy", fecha.getFullYear())
        .replace("MM", mes)
        .replace("dd", dia);
    
    return nueva_fecha
}

const obj_transaccion = ref({
    id: "",
    monto: 1,
    ordenante: "",
    fecha: hoy(),
    cuentaOrdenante: "",
    perfilOrdenante: "",
    cuentaBeneficiaria: "",
    perfilBeneficiario: "",
    descripcion: ""
})
</script>