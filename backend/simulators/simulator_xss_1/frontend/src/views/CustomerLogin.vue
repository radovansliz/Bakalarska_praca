<template>
  <div class="w-full h-full overflow-y-auto p-4 bg-white lg:px-8">
    <div class="flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-md">
        <h2
          class="mt-6 text-center text-3xl font-bold tracking-tight text-gray-700"
        >
          Sign in to your customer account
        </h2>
      </div>

      <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div class="bg-primary-100 py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <div class="space-y-6">
            <div>
              <label for="email" class="block text-sm font-medium text-gray-600"
                >Email address</label
              >
              <div class="mt-1">
                <input
                  id="email"
                  name="email"
                  v-model="signInForm.email"
                  class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-button-color focus:outline-none focus:ring-button-color sm:text-sm"
                />
              </div>
            </div>

            <div>
              <label
                for="password"
                class="block text-sm font-medium text-gray-600"
                >Password</label
              >
              <div class="mt-1">
                <input
                  id="password"
                  name="password"
                  v-model="signInForm.password"
                  class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-button-color focus:outline-none focus:ring-button-color sm:text-sm"
                />
              </div>
            </div>

            <div class="flex items-center justify-between">
              <div class="flex items-center">
                <input
                  id="remember-me"
                  name="remember-me"
                  type="checkbox"
                  class="h-4 w-4 rounded border-gray-300 text-button-color focus:ring-button-color"
                />
                <label
                  for="remember-me"
                  class="ml-2 block text-sm text-gray-600"
                  >Remember me</label
                >
              </div>

              <div class="text-sm">
                <a
                  href="#"
                  class="font-medium text-button-color hover:text-button-color"
                  >Forgot your password?</a
                >
              </div>
            </div>

            <div>
              <button
                class="flex w-full justify-center rounded-md border border-transparent bg-button-color py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-button-color focus:outline-none focus:ring-2 focus:ring-button-color focus:ring-offset-2"
                >
                Sign in
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="response">
      <InfoAlert :content="response"></InfoAlert>
    </div>
  </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import InfoAlert from '@/components/InfoAlert.vue'
import { useApiFetch } from '@/composables/useApi';

const router = useRouter()
const response: any = ref(null)
const loader = ref(false)
const signInForm = ref({
  email: '',
  password: '',
})


const goBack = () => {
  router.go(-1)
}
</script>
