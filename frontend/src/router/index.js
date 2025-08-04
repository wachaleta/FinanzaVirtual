import { createRouter, createWebHistory } from "vue-router";

import authRoutes from "./auth.routes"
import perfilRoutes from "./perfil.routes"
import transaccionRoutes from "./transaccion.routes"

const baseRoutes = []

const routes = baseRoutes
.concat(perfilRoutes)
.concat(authRoutes)
.concat(transaccionRoutes)


const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
    if(to.meta.requiresAuth && localStorage.getItem("access") == null) { 
        next({ 
            name: 'login',
            query: {
                nextUrl: to.name
            }
        })
    } else {
        next()
    }
})

export default router