import NotFound from '@/views/NotFoundView.vue'
import { RouteRecordRaw } from 'vue-router'

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
  { path: '/:path(.*)', component: NotFound },
]
