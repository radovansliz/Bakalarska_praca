<template>
  <div class="w-full h-full overflow-y-auto p-4 bg-dark-400 lg:px-8">
    <div class="py-6 overflow-hidden px-4 sm:px-6 lg:px-8 flex">
      <div class="relative mx-auto max-w-xl">
        <div class="text-center">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">
            I am interested in a mortgage
          </h2>
          <p class="mt-4 text-lg leading-6 text-gray-200">
            Please fill contact form and our specialist will contact you soon
          </p>
        </div>
        <div class="mt-5">
          <form
            action="#"
            method="POST"
            class="grid grid-cols-1 gap-y-6 sm:grid-cols-2 sm:gap-x-8"
          >
            <div>
              <label
                for="first-name"
                class="block text-sm font-medium text-gray-100"
                >First name</label
              >
              <div class="mt-1">
                <input
                  type="text"
                  name="first-name"
                  id="first-name"
                  autocomplete="given-name"
                  class="block w-full rounded-md border-gray-300 py-3 px-4 shadow-sm focus:border-button-color focus:ring-button-color"
                />
              </div>
            </div>
            <div>
              <label
                for="last-name"
                class="block text-sm font-medium text-gray-100"
                >Last name</label
              >
              <div class="mt-1">
                <input
                  type="text"
                  name="last-name"
                  id="last-name"
                  autocomplete="family-name"
                  class="block w-full rounded-md border-gray-300 py-3 px-4 shadow-sm focus:border-button-color focus:ring-button-color"
                />
              </div>
            </div>
            <div class="sm:col-span-2">
              <label
                for="address"
                class="block text-sm font-medium text-gray-100"
                >Address</label
              >
              <div class="mt-1">
                <input
                  type="text"
                  name="address"
                  id="address"
                  autocomplete="address"
                  class="block w-full rounded-md border-gray-300 py-3 px-4 shadow-sm focus:border-button-color focus:ring-button-color"
                />
              </div>
            </div>
            <div class="sm:col-span-2">
              <label for="email" class="block text-sm font-medium text-gray-100"
                >Email</label
              >
              <div class="mt-1">
                <input
                  id="email"
                  name="email"
                  type="email"
                  autocomplete="email"
                  class="block w-full rounded-md border-gray-300 py-3 px-4 shadow-sm focus:border-button-color focus:ring-button-color"
                />
              </div>
            </div>
            <div class="sm:col-span-2">
              <label
                for="phone-number"
                class="block text-sm font-medium text-gray-100"
                >Phone Number</label
              >
              <div class="relative mt-1 rounded-md shadow-sm">
                <div class="absolute inset-y-0 left-0 flex items-center">
                  <label for="country" class="sr-only">Country</label>
                  <select
                    id="country"
                    name="country"
                    class="h-full rounded-md border-transparent bg-transparent py-0 pl-4 pr-8 text-gray-500 focus:border-button-color focus:ring-button-color"
                  >
                    <option>US</option>
                    <option>CA</option>
                    <option>EU</option>
                  </select>
                </div>
                <input
                  type="text"
                  name="phone-number"
                  id="phone-number"
                  autocomplete="tel"
                  class="block w-full rounded-md border-gray-300 py-3 px-4 pl-20 focus:border-button-color focus:ring-button-color"
                  placeholder="+1 (555) 987-6543"
                />
              </div>
            </div>
            <div class="sm:col-span-2">
              <label
                for="message"
                class="block text-sm font-medium text-gray-100"
                >Message</label
              >
              <div class="mt-1">
                <textarea
                  id="message"
                  name="message"
                  rows="4"
                  class="block w-full rounded-md border-gray-300 py-3 px-4 shadow-sm focus:border-button-color focus:ring-button-color"
                />
              </div>
            </div>
            <div class="sm:col-span-2">
              <div class="flex items-start">
                <div class="flex-shrink-0">
                  <Switch
                    v-model="agreed"
                    :class="[
                      agreed ? 'bg-button-color' : 'bg-gray-200',
                      'relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-button-color focus:ring-offset-2'
                    ]"
                  >
                    <span class="sr-only">Agree to policies</span>
                    <span
                      aria-hidden="true"
                      :class="[
                        agreed ? 'translate-x-5' : 'translate-x-0',
                        'inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out'
                      ]"
                    />
                  </Switch>
                </div>
                <div class="ml-3">
                  <p class="text-base text-gray-500">
                    By selecting this, you agree to the
                    {{ ' ' }}
                    <a href="#" class="font-medium text-gray-100 underline"
                      >Privacy Policy</a
                    >
                    {{ ' ' }}
                    and
                    {{ ' ' }}
                    <a href="#" class="font-medium text-gray-100 underline"
                      >Cookie Policy</a
                    >.
                  </p>
                </div>
              </div>
            </div>
            <div class="sm:col-span-2">
              <button
                type="submit"
                class="inline-flex w-full items-center justify-center rounded-md border border-transparent bg-button-color px-6 py-3 text-base font-medium text-white shadow-sm hover:bg-button-color focus:outline-none focus:ring-2 focus:ring-button-color focus:ring-offset-2"
              >
                Send request
              </button>
            </div>
          </form>
        </div>
      </div>
      <div v-if="response" class="">
        <InfoAlert :content="response"></InfoAlert>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { Switch } from '@headlessui/vue'
import InfoAlert from '@/components/InfoAlert.vue'

const router = useRouter()
const agreed = ref(false)
const response = ref(null)

const results = {
  results: [
    {
      response: [
        [
          'John Smith',
          '123-456-7890',
          '123 Main St',
          'johnsmith@email.com',
          'savings',
          '2020-01-01T00:00:00',
          true,
          false
        ],
        [
          'Jane Doe',
          '123-456-7891',
          '456 Main St',
          'janedoe@email.com',
          'checking',
          '2020-02-01T00:00:00',
          true,
          true
        ],
        [
          'Bob Johnson',
          '123-456-7892',
          '789 Main St',
          'bobjohnson@email.com',
          'savings',
          '2020-03-01T00:00:00',
          false,
          true
        ],
        [
          'Sally Smith',
          '123-456-7893',
          '321 Main St',
          'sallysmith@email.com',
          'checking',
          '2020-04-01T00:00:00',
          false,
          false
        ],
        [
          'Mike Jones',
          '123-456-7894',
          '654 Main St',
          'mikejones@email.com',
          'savings',
          '2020-05-01T00:00:00',
          true,
          true
        ],
        [
          'Lisa Williams',
          '123-456-7895',
          '987 Main St',
          'lisawilliams@email.com',
          'checking',
          '2020-06-01T00:00:00',
          false,
          true
        ],
        [
          'Chris Brown',
          '123-456-7896',
          '246 Main St',
          'chrisbrown@email.com',
          'savings',
          '2020-07-01T00:00:00',
          true,
          true
        ],
        [
          'Sarah Johnson',
          '123-456-7897',
          '369 Main St',
          'sarahjohnson@email.com',
          'checking',
          '2020-08-01T00:00:00',
          false,
          false
        ],
        [
          'Tom Smith',
          '123-456-7898',
          '159 Main St',
          'tomsmith@email.com',
          'savings',
          '2020-09-01T00:00:00',
          true,
          true
        ],
        [
          'Kate Williams',
          '123-456-7899',
          '753 Main St',
          'katewilliams@email.com',
          'checking',
          '2020-10-01T00:00:00',
          true,
          true
        ],
        [
          'Mark Jones',
          '123-456-7900',
          '147 Main St',
          'markjones@email.com',
          'savings',
          '2020-11-01T00:00:00',
          false,
          true
        ]
      ],
      query: "SELECT * FROM clients WHERE name = ''; Select * from clients;"
    },
    {
      response: {},
      query: "SELECT * FROM clients WHERE name = '4564654"
    },
    {
      response: {},
      query: "SELECT * FROM clients WHERE name = 'Hlavna"
    },
    {
      response: {},
      query: "SELECT * FROM clients WHERE name = 'jozef@gmail.com"
    },
    {
      response: {},
      query: "SELECT * FROM clients WHERE name = 'Basic"
    },
    {
      response: {},
      query: "SELECT * FROM clients WHERE name = '2020-02-01 00:00:00"
    },
    {
      response: {},
      query: "SELECT * FROM clients WHERE name = 'False"
    },
    {
      response: {},
      query: "SELECT * FROM clients WHERE name = 'True"
    }
  ]
}

const goBack = () => {
  router.go(-1)
}
</script>
