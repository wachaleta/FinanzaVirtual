import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import router from './router/'
import Vue3Toastify, { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css';
import filters from '@/filters'
import {
    focus
} from '@/directives'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import 'vue-multiselect/dist/vue-multiselect.min.css'

const pinia = createPinia()

const appInstance = createApp(App)

appInstance.use(Vue3Toastify, {
    transition: toast.TRANSITIONS.SLIDE,
    position: toast.POSITION.BOTTOM_RIGHT,
    theme: toast.THEME.COLORED,
    pauseOnFocusLoss: false,
    multiple: true,
})
appInstance.use(router)
appInstance.use(pinia)

appInstance.config.globalProperties.$filters = filters

appInstance.directive("focus", focus)

appInstance.mount('#app')