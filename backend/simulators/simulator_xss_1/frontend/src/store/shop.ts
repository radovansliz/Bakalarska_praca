import { defineStore } from 'pinia'
import sanitizeHTML from 'sanitize-html'

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
      ],
      numberOfInputs: 10
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
    getVulnerableInputNumber(state) {
      return import.meta.env.VITE_AIS_ID % state.numberOfInputs === 0
        ? state.numberOfInputs
        : import.meta.env.VITE_AIS_ID % state.numberOfInputs
    },
    isInputVulnerable(state) {
      return (id: string): any =>
        id.toString() === this.getVulnerableInputNumber.toString()
    }
  },

  actions: {
    processValue(inputObject: { id: string; value: any }) {
      if (this.isInputVulnerable(inputObject.id)) {
        return inputObject.value
      } else {
        return sanitizeHTML(inputObject.value)
          ? sanitizeHTML(inputObject.value)
          : 'Nothing to show'
      }
    }
  }
})
