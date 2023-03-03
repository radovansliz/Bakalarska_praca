import type { Router, RouteRecordName } from 'vue-router'

const noAuthWhitelist: RouteRecordName[] = [
  'signup',
  'login',
  'index',
  'auth',
  'blog',
  'products',
  'landing'
]

export default function useAuthGuard(router: Router) {
  // Authguard
}
