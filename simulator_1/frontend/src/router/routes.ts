import NotFound from '@/views/NotFoundView.vue'
import { RouteLocationNormalizedLoaded, RouteRecordRaw } from 'vue-router'
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
      return { path: '/products' }
    }
  },
  {
    name: 'products',
    path: '/products',
    component: () => import('@/views/ProductsView.vue'),
    meta: {
      title: 'ProductList',
      layout: ''
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
