import type { Router, RouteRecordName } from 'vue-router'

const noAuthWhitelist: RouteRecordName[] = [
  'index',
  'auth',
]

export default function useAuthGuard(router: Router) {
  router.beforeEach(async (to: any, from: any, next) => {
    try {
      // wait for signIn status which is assigned asynchronously
      // Sign in is not implemented
      next()
    } catch (error) {
      if (noAuthWhitelist.includes(to.name)) {
        next()
      } else {
        next({ name: 'login' })
      }
    }
  })
}
