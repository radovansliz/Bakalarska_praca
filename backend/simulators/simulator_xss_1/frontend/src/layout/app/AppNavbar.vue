<template>
  <Disclosure
    as="nav"
    class="bg-primary-600 top-0 z-10 sticky"
    v-slot="{ open }"
  >
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <!-- Mobile menu button-->
          <DisclosureButton
            class="inline-flex items-center justify-center rounded-md p-2 text-white hover:bg-primary-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
          >
            <span class="sr-only">Open main menu</span>
            <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
        <div
          class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start"
        >
          <div class="hidden sm:ml-6 sm:block">
            <div class="flex space-x-4">
              <div
                v-for="item in navigation"
                :key="item.name"
                :class="[
                  item.routeName === route.name
                    ? 'bg-primary-500 text-white'
                    : 'text-white hover:bg-primary-500 hover:text-white cursor-pointer',
                  'px-3 py-2 rounded-md text-sm font-medium'
                ]"
                :aria-current="item.current ? 'page' : undefined"
                @click="routeTo(item.routeName)"
              >
                {{ item.name }}
              </div>
            </div>
          </div>
        </div>
        <div
          class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
        >
          <button
            type="button"
            class="rounded-ful p-1 text-white hover:text-white"
          >
            <QuestionMarkCircleIcon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
      </div>
    </div>

    <DisclosurePanel class="sm:hidden">
      <div class="space-y-1 px-2 pt-2 pb-3">
        <DisclosureButton
          v-for="item in navigation"
          :key="item.name"
          as="a"
          :href="item.href"
          :class="[
            route.name === item.name
              ? 'bg-primary-900 text-white'
              : 'text-white hover:bg-primary-700 hover:text-white',
            'block px-3 py-2 rounded-md text-base font-medium'
          ]"
          :aria-current="item.current ? 'page' : undefined"
          >{{ item.name }}</DisclosureButton
        >
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>
<script setup lang="ts">
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems
} from '@headlessui/vue'
import {
  Bars3Icon,
  BellIcon,
  XMarkIcon,
  QuestionMarkCircleIcon
} from '@heroicons/vue/24/outline'
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()

function routeTo(route: string) {
  router.push({ name: route })
}

const navigation = [
  { name: 'Home', routeName: 'landing', href: '/landing', current: true },
  {
    name: 'Products',
    routeName: 'products',
    href: '/products',
    current: false
  },
  {
    name: 'Customer Account',
    routeName: 'account',
    href: '/account',
    current: false
  },
  { name: 'Support', routeName: 'support', href: '/support', current: false }
]
</script>

<style lang="scss" scoped></style>
