import { markRaw } from 'vue'
import router from '@/router/index'
import { defineStore, createPinia } from 'pinia'

const useRouter = markRaw(router)

export const useShopStore = defineStore('shop', {
  state: () => {
    return {
      auth: false,
      cart: [] as any[],
      products: [
        {
          id: 1,
          name: 'Machined Pen',
          color: 'Black',
          price: '$35',
          href: '/products/1',
          imageSrc:
            'https://tailwindui.com/img/ecommerce-images/home-page-02-product-01.jpg',
          imageAlt:
            'Black machined steel pen with hexagonal grip and small white logo at top.',
          availableColors: [
            { name: 'Black', colorBg: '#111827' },
            { name: 'Brass', colorBg: '#FDE68A' },
            { name: 'Chrome', colorBg: '#E5E7EB' }
          ]
        },
        {
          id: 2,
          name: 'Mug',
          color: 'Matte black',
          price: '$28',
          href: '/products/2',
          imageSrc:
            'https://tailwindui.com/img/ecommerce-images/home-page-02-product-02.jpg',
          imageAlt:
            'Black porcelain mug with modern square handle and natural clay accents on rim and bottom.',
          availableColors: [
            { name: 'Black', colorBg: '#111827' },
            { name: 'Brass', colorBg: '#FDE68A' }
          ]
        },
        {
          id: 3,
          name: 'Leatherbound Daily Journal Set',
          color: 'Natural',
          price: '$50',
          href: '/products/3',
          imageSrc:
            'https://tailwindui.com/img/ecommerce-images/home-page-02-product-03.jpg',
          imageAlt:
            'Natural leather journal with brass disc binding and three paper refill sets.',
          availableColors: [
            { name: 'Black', colorBg: '#111827' },
            { name: 'Brass', colorBg: '#FDE68A' },
            { name: 'Chrome', colorBg: '#E5E7EB' }
          ]
        },
        {
          id: 4,
          name: 'Leatherbound Daily Journal',
          color: 'Black',
          price: '$50',
          href: '/products/4',
          imageSrc:
            'https://tailwindui.com/img/ecommerce-images/home-page-02-product-04.jpg',
          imageAlt: 'Black leather journal with brass disc binding.',
          availableColors: [
            { name: 'Black', colorBg: '#111827' },
            { name: 'Brass', colorBg: '#FDE68A' },
            { name: 'Chrome', colorBg: '#E5E7EB' }
          ]
        }
      ]
    }
  },

  getters: {
    isSigned: (state) => state.auth,
    cartItems: (state) => state.cart,
    produtItems: (state) => state.products,
    getProductById(state) {
      return (id: string | number): any =>
        state.products.find((product: any) => product.id === id)
    }
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
