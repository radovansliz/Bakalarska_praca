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
                  v-model="signInForm.email.value"
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
                  v-model="signInForm.password.value"
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
                @click="submitInput"
              >
                Sign in
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showComponent" class="w-full">
      <!-- RESULT Frame -->
      <ResultFrame
        v-for="input in Object.values(signInForm)"
        :key="input.id"
        :result="input.result"
        :isInputVulnerable="shopStore.isInputVulnerable(input.id)"
        :showComponent="showComponent"
        :flagFound="flagFound"
        :flag="flag"
        :title="input.title"
      ></ResultFrame>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'
import useFlagMethods from '@/composables/useFlagMethods'
import { useShopStore } from '@/store/shop'
import ResultFrame from '@/components/ResultFrame.vue'

const shopStore = useShopStore()
const showComponent = ref(false)

const signInForm = ref({
  email: {
    id: '2',
    value: '',
    title: 'email',
    result: null
  },
  password: {
    id: '3',
    value: '',
    title: 'password',
    result: null
  }
})

// Composable to import vulnerable logic to call flag. getFlag method is called dynamically it is not used nowhere in code
const { flagFound, flag, getFlag } = useFlagMethods()

// Method to process input in store
function submitInput() {
  showComponent.value = false
  flag.value = ''
  flagFound.value = false

  Object.values(signInForm.value).map((element) => {
    setTimeout(() => {
      element.result = shopStore.processValue({
        id: element.id,
        value: element.value
      })
    })
  })
  showComponent.value = true
}
</script>
