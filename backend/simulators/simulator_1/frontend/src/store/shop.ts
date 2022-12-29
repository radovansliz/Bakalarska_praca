import { markRaw } from 'vue'
import router from '@/router/index'
import { defineStore, createPinia } from 'pinia'

const useRouter = markRaw(router)

export const useShopStore = defineStore('shop', {
  state: () => {
    return {
      auth: false,
      cart: [] as any[]
    }
  },

  getters: {
    isSigned: (state) => state.auth,
    cartItems: (state) => state.cart
  },

  actions: {
    async signIn(user: any, token: any): Promise<void> {
      return Promise.resolve()
    },

    async signOut(): Promise<void> {
      console.log('SIGN OUT')
    },

    async addToCart(item: any): Promise<void> {
      this.cart.push(item)
    },

    async removeFromCart(itemId: string): Promise<void> {
      if (this.cart.length > 0) {
        const index = this.cart.indexOf((item: any) => item.id === itemId)
        if (index > 0) {
          this.cart.splice(index, 1)
        }
      }
    }
  }
})
