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
    name: 'account',
    path: '/account',
    component: () => import('@/views/CustomerLogin.vue'),
    meta: {
      title: 'CustomerLoginView',
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
    path: '/products/:id',
    component: () => import('@/views/ProductDetailView.vue'),
    meta: {
      title: 'ProductDetail',
      layout: AppLayout
    }
  },
  {
    name: 'support',
    path: '/support',
    component: () => import('@/views/SupportView.vue'),
    meta: {
      title: 'SupportView',
      layout: AppLayout
    }
  },
  { path: '/:path(.*)', component: NotFound }
]
