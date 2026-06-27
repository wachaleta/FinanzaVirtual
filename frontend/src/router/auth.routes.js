import { 
    LoginView,
    RegisterView,
} from "@/components/auth"

export default [
    {
        path: '/login', 
        name: 'login',
        component: LoginView,
        meta: {
            keepQuery: true
        }
    },
    {
        path: '/register', 
        name: 'register',
        component: RegisterView,
        meta: {
            requiresAuth: false,
            keepQuery: true,
            ignoreFromNextUrl: true,
        }
    },
]