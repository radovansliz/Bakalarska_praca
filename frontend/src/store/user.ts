import { markRaw } from 'vue'
import router from '@/router/index'
import { defineStore, createPinia } from 'pinia'


const useRouter = markRaw(router)

export const useUserStore = defineStore('user', {
  state: () => {
    return {
      auth: false,
    }
  },

  getters: {},

  actions: {},
})
