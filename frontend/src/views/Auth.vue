<template>
  <div class="flex min-h-full">
    <div
      class="flex flex-1 w-full flex-col justify-center py-12 px-4 sm:px-6 lg:flex-none lg:px-12 xl:px-12"
    >
      <div v-if="simulatorResponse === null" class="mx-auto w-full max-w-md">
        <div>
          <h2 class="mt-6 text-3xl font-bold tracking-tight text-gray-900">
            {{ $t('initView.title') }}
          </h2>
        </div>

        <div class="mt-8">
          <div class="mt-6">
            <div>
              <label
                for="email"
                class="block text-sm font-medium text-gray-700"
              >
                {{ $t('initView.aisId') }}
              </label>
              <div class="mt-1">
                <input
                  v-model="aisId"
                  id="asiId"
                  name="asiId"
                  type="number"
                  class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                />
              </div>
              <div v-if="enterIdError" class="w-full mt-1 text-xs text-red-600">
                {{ $t('initView.validError') }}
              </div>
            </div>
            <div>
              <button
                @click="startSimulator"
                class="mt-4 flex w-full justify-center rounded-md border border-transparent bg-primary-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
              >
                <LoadingIcon
                  v-if="loading"
                  class="-ml-1 mr-3 h-5 w-5 text-white"
                />
                <slot />
                {{ $t('initView.start') }}
              </button>
              <div
                v-if="loading"
                class="w-full flex items-center text-xs font-sans text-primary-500 mt-3"
              >
                {{ $t('initView.startingSimulator') }}
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="mx-auto w-full max-w-md">
        <div class="bg-white">
          <div class="mx-auto max-w-7xl py-16 px-6 sm:py-24 lg:px-8">
            <div class="text-center">
              <h2 class="text-base font-semibold text-primary-600">
                {{ $t('initView.simulatorUpTitle') }}
              </h2>
              <p class="mt-1 text-4xl font-bold tracking-tight text-gray-900">
                {{ $t('initView.simulatorReady') }}
              </p>
              <p class="mx-auto mt-5 max-w-xl text-base text-gray-500">
                {{ $t('initView.enterSimulator') }}
              </p>
              <div
                class="mt-5 w-full flex items-ceneter justify-center space-x-5"
              >
                <button
                  @click="stopSimulator"
                  class="flex justify-center rounded-md border border-primary-700 bg-white py-2 px-4 text-sm font-medium text-primary-700 shadow-sm hover:bg-white focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
                >
                  <LoadingIcon
                    v-if="loading"
                    class="-ml-1 mr-3 h-5 w-5 text-primary-700"
                  />
                  <slot />
                  {{ $t('initView.stop') }}
                </button>
                <a
                  v-if="!loading"
                  :href="simulatorResponse.url"
                  target="_blank"
                  class="inline-flex items-center rounded-md border border-transparent bg-primary-600 px-8 py-2 text-sm font-medium text-white shadow-sm hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
                >
                  {{ $t('initView.continue') }}
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { useApiFetch } from '@/composables/useApi'
import { ref } from 'vue'
import LoadingIcon from '@/components/LoadingIcon.vue'

const loading = ref(false)

const aisId = ref(null)
const enterIdError = ref(false)
const simulatorResponse: any = ref(null)

async function startSimulator() {
  enterIdError.value = false
  if (!aisId.value) {
    enterIdError.value = true
    return
  }

  loading.value = true

  const { response, data } = await useApiFetch('start')
    .post({
      id: aisId.value
    })
    .json()

  // Timeout added to wait until simulator docker container is ready
  setTimeout(() => {}, 2000)

  simulatorResponse.value = data.value
  aisId.value = null
  loading.value = false
  console.log('STATUS CODE', response.value)
}

async function stopSimulator() {
  loading.value = true

  const { response } = await useApiFetch('stop').get()

  simulatorResponse.value = null

  loading.value = false
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
