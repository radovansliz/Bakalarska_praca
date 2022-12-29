import NotFound from '@/views/NotFoundView.vue'
import { RouteLocationNormalizedLoaded, RouteRecordRaw } from 'vue-router'
import AppLayout from '@/layout/app/AppLayout.vue'
/**
 * Makes sure that the view is not refreshed when tabs are clicked in a source detail.
 * @see SourceDetailView.vue
 */
const syncSourceDetailWithTab = (route: RouteLocationNormalizedLoaded) =>
  `source-custom-${route.params.id}`

export const routes: RouteRecordRaw[] = [
  {
    name: 'index',
    path: '/',
    redirect: () => {
      return { name: 'landing' }
    }
  },
  {
    name: 'landing',
    path: '/landing',
    component: () => import('@/views/LandingView.vue'),
    meta: {
      title: 'LandingView',
      layout: AppLayout
    }
  },
  {
    name: 'mortgage',
    path: '/mortgage',
    component: () => import('@/views/MortgageView.vue'),
    meta: {
      title: 'MortgageView',
      layout: AppLayout
    }
  },
  {
    name: 'account',
    path: '/account',
    component: () => import('@/views/BankAccountView.vue'),
    meta: {
      title: 'BankAccountView',
      layout: AppLayout
    }
  },
  {
    name: 'products',
    path: '/products',
    component: () => import('@/views/ProductsView.vue'),
    meta: {
      title: 'ProductList',
      layout: AppLayout
    }
  },
  {
    name: 'product_detail',
    path: '/product/id:',
    component: () => import('@/views/ProductDetailView.vue'),
    meta: {
      title: 'ProductDetail',
      layout: ''
    }
  },
  {
    name: 'support',
    path: '/support',
    component: () => import('@/views/SupportView.vue'),
    meta: {
      title: 'Support',
      layout: ''
    }
  },
  { path: '/:path(.*)', component: NotFound }
]
