<template>
  <div class="bg-dark-400">
    <div class="mx-auto max-w-7xl py-12 lg:flex lg:items-center lg:py-16">
      <div class="lg:w-0 lg:flex-1">
        <h2
          class="text-xl font-bold tracking-tight text-white"
          id="newsletter-headline"
        >
          Stay in touch
        </h2>
        <p class="mt-3 max-w-3xl text-base leading-6 text-gray-300">
          I want to get updates about new products and offers. I want to recieve
          emails with offers and newsletter
        </p>
      </div>
      <div class="mt-8 lg:mt-0 lg:ml-8">
        <div class="sm:flex">
          <label for="email-address" class="sr-only">Email address</label>
          <input
            type="text"
            v-model="newsletterForm.email.value"
            class="w-full rounded-md border border-transparent px-5 py-3 placeholder-gray-500 focus:border-white focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800 sm:max-w-xs"
            placeholder="Enter your email"
          />
          <div class="mt-3 rounded-md shadow sm:mt-0 sm:ml-3 sm:flex-shrink-0">
            <button
              class="flex w-full items-center justify-center rounded-md border border-transparent bg-button-color px-5 py-3 text-base font-medium text-white hover:bg-button-color focus:outline-none focus:ring-2 focus:ring-button-color focus:ring-offset-2 focus:ring-offset-gray-800"
              @click="sendRequest(newsletterForm)"
            >
              <LoadingIcon
                v-if="loading"
                class="-ml-1 mr-3 h-5 w-5 text-white"
              />
              <slot />
              Notify me
            </button>
          </div>
        </div>
        <p class="mt-3 text-sm text-gray-300">
          We care about the protection of your data. Read our
          {{ ' ' }}
          <a href="#" class="font-medium text-white underline"
            >Privacy Policy.</a
          >
        </p>
      </div>
    </div>
    <div v-if="response" class="mt-1">
      <InfoAlert :content="response"></InfoAlert>
    </div>
  </div>
</template>
<script setup lang="ts">
import InfoAlert from '@/components/InfoAlert.vue'
import { ref } from 'vue'
import useSendRequest from '@/composables/useSendRequest'
import LoadingIcon from '@/components/LoadingIcon.vue'

const newsletterForm = ref({
  email: {
    id: 1,
    name: 'Email',
    value: ''
  }
})

const { response, loading, sendRequest } = useSendRequest()
</script>
