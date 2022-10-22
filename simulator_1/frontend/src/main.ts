import { createApp } from 'vue'
import './tailwind.css'

// @ts-ignore
import App from './App.vue'
import router from './router'

// import Pinia store
import { createPinia } from 'pinia'

const app = createApp(App)

app.use(router)

const pinia = createPinia()
app.use(pinia)

// locale
import i18n from './locale'
app.use(i18n)


app.mount('#app')
