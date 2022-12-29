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
  // router.beforeEach(async (to: any, from: any, next) => {
  //   // const { isSigned, authSyncedAtLeastOnce } = storeToRefs(useUserStore())
  //   try {
  //     // wait for signIn status which is assigned asynchronously
  //     if (false) {
  //       if (['login', 'signup'].includes(to.name)) {
  //         next({ name: 'index' })
  //       } else {
  //         next()
  //       }
  //     } else {
  //       throw new Error('not-logged-iUser is not logged in')
  //     }
  //   } catch (error) {
  //     if (noAuthWhitelist.includes(to.name)) {
  //       next()
  //     } else {
  //       next({ name: 'login' })
  //     }
  //   }
  // })
}
