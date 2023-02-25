import { markRaw } from 'vue'
import router from '@/router/index'
import { defineStore, createPinia } from 'pinia'
import sanitizeHTML from 'sanitize-html'
import { useApiFetch } from '@/composables/useApi'

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
    },
    isInputVulnerable(state) {
      return (id: string): any => id === '1'
    }
  },

  actions: {
    processValue(inputObject: { id: string; value: any }) {
      console.log('INPUT OBJECT', inputObject)
      if (inputObject.id === '1') {
        console.log(
          'INPUT OBJECT RAW',
          inputObject.value.replace(/<script[^>]*>([\s\S]*?)<\/script>/g, '$1')
        )
        return inputObject.value.replace(
          /<script[^>]*>([\s\S]*?)<\/script>/g,
          '$1'
        )
      } else {
        console.log('INPUT OBJECT SANITIZED', sanitizeHTML(inputObject))
        return sanitizeHTML(inputObject.value) !== ''
          ? sanitizeHTML(inputObject.value)
          : 'Nothing to show'
      }
    },

    // API Method to get Flag
    async sendRequest() {
      flagFound.value = false
      // call api
      try {
        const { data: apiData, error: renormalizeError } = await useApiFetch(
          'flag'
        )
          .get()
          .json()
        if (renormalizeError.value) {
          flag.value = renormalizeError.value
        } else {
          flagFound.value = true
          flag.value = apiData.value.detail[0][0]
        }
      } catch (e) {
        flag.value = 'Error'
      }
    }
  }
})
