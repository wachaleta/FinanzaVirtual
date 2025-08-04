import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import router from './router/'
import store from './store'
import Vue3Toastify, { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css';

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

const pinia = createPinia()

createApp(App)
// .use(store)
    .use(Vue3Toastify, {
        transition: toast.TRANSITIONS.SLIDE,
        position: toast.POSITION.BOTTOM_RIGHT,
        theme: toast.THEME.COLORED,
        pauseOnFocusLoss: false,
        multiple: true,
    })
    .use(router)
    .use(pinia)
    .mount('#app')
