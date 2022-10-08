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

  getters: {
    isSigned: (state) => state.auth,
  },

  actions: {
    async signIn(user: any, token: any): Promise<void> {
      return Promise.resolve()
    },

    async signOut(): Promise<void> {
      console.log('SIGN OUT')
    },
  },
})
