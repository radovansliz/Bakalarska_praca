<template>
  <div class="bg-white px-4 py-5 sm:rounded-lg sm:p-6">
    <div class="md:grid md:grid-cols-1 md:gap-6">
      <div class="mt-5 md:col-span-2 md:mt-0">
        <div class="grid grid-cols-6 gap-6">
          <div class="col-span-6">
            <section aria-labelledby="notes-title">
              <div class="bg-white shadow sm:overflow-hidden sm:rounded-lg">
                <div class="divide-y divide-gray-200">
                  <div class="px-4 py-5 sm:px-6">
                    <h2
                      id="notes-title"
                      class="text-lg font-medium text-gray-900"
                    >
                      Contribute
                    </h2>
                  </div>
                </div>
                <div class="w-full p-5 space-y-4">
                  <div class="col-span-6 sm:col-span-3">
                    <label
                      for="first-name"
                      class="block text-sm font-medium text-gray-700"
                      >First name</label
                    >
                    <input
                      type="text"
                      name="first-name"
                      id="first-name"
                      autocomplete="given-name"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    />
                  </div>

                  <div class="col-span-6 sm:col-span-3">
                    <label
                      for="last-name"
                      class="block text-sm font-medium text-gray-700"
                      >Last name</label
                    >
                    <input
                      type="text"
                      name="last-name"
                      id="last-name"
                      autocomplete="family-name"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    />
                  </div>

                  <div class="col-span-6 sm:col-span-4">
                    <label
                      for="email-address"
                      class="block text-sm font-medium text-gray-700"
                      >Email address</label
                    >
                    <input
                      type="text"
                      name="email-address"
                      id="email-address"
                      autocomplete="email"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    />
                  </div>

                  <div class="col-span-6 sm:col-span-3">
                    <label
                      for="country"
                      class="block text-sm font-medium text-gray-700"
                      >Category</label
                    >
                    <select
                      id="country"
                      name="country"
                      autocomplete="country-name"
                      class="mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                    >
                      <option>Support</option>
                      <option>Delivery</option>
                      <option>Technical problems</option>
                    </select>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-6 sm:px-6">
                  <div class="flex space-x-3">
                    <div class="flex-shrink-0"></div>
                    <div class="min-w-0 flex-1">
                      <form action="#">
                        <div>
                          <label for="comment" class="sr-only">About</label>
                          <textarea
                            id="comment"
                            name="comment"
                            rows="3"
                            class="block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
                            placeholder="Add a note"
                          />
                        </div>
                        <div class="mt-3 flex items-center justify-between">
                          <div></div>
                          <button
                            type="submit"
                            class="inline-flex items-center justify-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
                          >
                            Comment
                          </button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </section>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const goBack = () => {
  router.go(-1)
}
</script>
