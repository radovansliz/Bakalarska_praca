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
      return { path: '/auth' }
    },
  },
  {
    name: 'auth',
    path: '/auth',
    component: () => import('@/views/Auth.vue'),
    meta: {
      title: 'Auth',
      layout: '',
    },
  },
  {
    name: 'blog',
    path: '/blog',
    component: () => import('@/views/Blog.vue'),
    meta: {
      title: 'Blog',
      layout: '',
    },
  },
  { path: '/:path(.*)', component: NotFound },
]
