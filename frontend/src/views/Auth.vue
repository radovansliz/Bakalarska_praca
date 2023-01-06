<template>
  <div class="flex min-h-full">
    <div
      class="flex flex-1 w-full flex-col justify-center py-12 px-4 sm:px-6 lg:flex-none lg:px-12 xl:px-12"
    >
      <div v-if="simulatorResponse === null" class="mx-auto w-full max-w-md">
        <div>
          <h2 class="mt-6 text-3xl font-bold tracking-tight text-gray-900">
            Enter AIS ID to start simulator
          </h2>
          <!-- <p class="mt-2 text-sm text-gray-600">
            Or
            {{ ' ' }}
            <a
              href="/blog"
              class="font-medium text-indigo-600 hover:text-indigo-500"
              >contact support</a
            >
          </p> -->
        </div>

        <div class="mt-8">
          <div class="mt-6">
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700"
                >AIS ID</label
              >
              <div class="mt-1">
                <input
                  v-model="aisId"
                  id="asiId"
                  name="asiId"
                  type="number"
                  required=""
                  class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                />
              </div>
              <div v-if="enterIdError" class="w-full mt-1 text-xs text-red-600">
                Enter valid AIS ID
              </div>
            </div>

            <!--              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <input
                    id="remember-me"
                    name="remember-me"
                    type="checkbox"
                    class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                  />
                  <label
                    for="remember-me"
                    class="ml-2 block text-sm text-gray-900"
                    >Remember me</label
                  >
                </div>

                <div class="text-sm">
                  <a
                    href="#"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                    >Forgot your password?</a
                  >
                </div>
              </div>-->

            <div>
              <button
                @click="startSimulator"
                class="mt-4 flex w-full justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
              >
                Start
              </button>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="mx-auto w-full max-w-md">
        <div class="bg-white">
          <div class="mx-auto max-w-7xl py-16 px-6 sm:py-24 lg:px-8">
            <div class="text-center">
              <h2 class="text-base font-semibold text-indigo-600">
                CTF Simulations
              </h2>
              <p
                class="mt-1 text-4xl font-bold tracking-tight text-gray-900"
              >
                Simulator is ready
              </p>
              <p class="mx-auto mt-5 max-w-xl text-base text-gray-500">
                Click the button below to enter the simulator
              </p>
              <div class="mt-5">
                <a
                  :href="simulatorResponse.url"
                  target="_blank"
                  class="inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                  >Continue</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useApiFetch } from '@/composables/useApi'
import { ref, reactive } from 'vue'

const router = useRouter()
const goBack = () => {
  router.go(-1)
}

const aisId = ref(null)
const enterIdError = ref(false)
const simulatorResponse: any = ref(null)

async function startSimulator() {
  enterIdError.value = false
  if (!aisId.value) {
    enterIdError.value = true
    return
  }

  const { response, data } = await useApiFetch('start')
    .post({
      id: aisId.value
    })
    .json()

  simulatorResponse.value = data.value

  console.log('STATUS CODE', response.value)
}
</script>
<style scoped>
/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type='number'] {
  -moz-appearance: textfield;
}
</style>
