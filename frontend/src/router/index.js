import { createRouter, createWebHistory } from "vue-router";

import authRoutes from "./auth.routes"
import cuentaRoutes from "./cuenta.routes";
import perfilRoutes from "./perfil.routes"
import transaccionRoutes from "./transaccion.routes"
import categoriaRoutes from "./categoria.routes";

const baseRoutes = []

const routes = baseRoutes
    .concat(perfilRoutes)
    .concat(cuentaRoutes)
    .concat(authRoutes)
    .concat(transaccionRoutes)
    .concat(categoriaRoutes)


const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth && localStorage.getItem("access") == null) {
        next({
            name: 'login',
            query: {
                nextUrl: to.name
            }
        })
    } else if (Object.keys(to.query).length === 0 && Object.keys(from.query).length > 0 && to.meta.keepQuery === true) {
        next({
            ...to,
            query: from.query
        })
    } else {
        next()
    }
})

export default router