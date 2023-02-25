<template>
  <div class="w-full overflow-y-auto p-4 bg-white">
    <main>
      <!-- Hero -->
      <div class="flex flex-col border-b border-gray-200 lg:border-0">
        <nav aria-label="Offers" class="order-last lg:order-first">
          <div class="mx-auto max-w-7xl lg:px-8">
            <ul
              role="list"
              class="grid grid-cols-1 divide-y divide-gray-200 lg:grid-cols-3 lg:divide-y-0 lg:divide-x"
            >
              <li
                v-for="offer in offers"
                :key="offer.name"
                class="flex flex-col"
              >
                <a
                  :href="offer.href"
                  class="relative flex flex-1 flex-col justify-center bg-white py-6 px-4 text-center focus:z-10"
                >
                  <p class="text-sm text-gray-500">{{ offer.name }}</p>
                  <p class="font-semibold text-gray-900">
                    {{ offer.description }}
                  </p>
                </a>
              </li>
            </ul>
          </div>
        </nav>

        <div class="relative">
          <div
            aria-hidden="true"
            class="absolute hidden h-full w-1/2 bg-gray-100 lg:block"
          />
          <div class="relative bg-gray-100 lg:bg-transparent">
            <div
              class="mx-auto max-w-7xl px-4 sm:px-6 lg:grid lg:grid-cols-2 lg:px-8"
            >
              <div class="mx-auto max-w-2xl py-24 lg:max-w-none lg:py-64">
                <div class="lg:pr-16">
                  <h1
                    class="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl xl:text-6xl"
                  >
                    Upgrade your home office with our accessories
                  </h1>
                  <p class="mt-4 text-xl text-gray-600">
                    Transform your workspace into a professional and efficient
                    environment with our range of office and home accessories
                  </p>
                  <div class="mt-6">
                    <a
                      href="/products"
                      class="inline-block rounded-md border border-transparent bg-primary-600 py-3 px-8 font-medium text-white hover:bg-primary-700"
                      >Shop Productivity</a
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div
            class="h-48 w-full sm:h-64 lg:absolute lg:top-0 lg:right-0 lg:h-full lg:w-1/2"
          >
            <img
              src="https://tailwindui.com/img/ecommerce-images/home-page-02-hero-half-width.jpg"
              alt=""
              class="h-full w-full object-cover object-center"
            />
          </div>
        </div>
      </div>

      <!-- Trending products -->
      <section aria-labelledby="trending-heading" class="bg-white">
        <div class="py-16 sm:py-24 lg:mx-auto lg:max-w-7xl lg:py-32 lg:px-8">
          <div class="flex items-center justify-between px-4 sm:px-6 lg:px-0">
            <h2
              id="trending-heading"
              class="text-2xl font-bold tracking-tight text-gray-900"
            >
              Trending products
            </h2>
            <a
              href="/products"
              class="hidden text-sm font-semibold text-primary-600 hover:text-primary-500 sm:block"
            >
              See everything
            </a>
          </div>

          <div class="relative mt-8">
            <div class="relative w-full overflow-x-auto">
              <ul
                role="list"
                class="mx-4 inline-flex space-x-8 sm:mx-6 lg:mx-0 lg:grid lg:grid-cols-4 lg:gap-x-8 lg:space-x-0"
              >
                <li
                  v-for="product in trendingProducts"
                  :key="product.id"
                  class="inline-flex w-64 flex-col text-center lg:w-auto"
                >
                  <div class="group relative">
                    <div
                      class="aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-md bg-gray-200"
                    >
                      <img
                        :src="product.imageSrc"
                        :alt="product.imageAlt"
                        class="h-full w-full object-cover object-center group-hover:opacity-75"
                      />
                    </div>
                    <div class="mt-6">
                      <p class="text-sm text-gray-500">{{ product.color }}</p>
                      <h3 class="mt-1 font-semibold text-gray-900">
                        <a :href="product.href">
                          <span class="absolute inset-0" />
                          {{ product.name }}
                        </a>
                      </h3>
                      <p class="mt-1 text-gray-900">{{ product.price }}</p>
                    </div>
                  </div>

                  <h4 class="sr-only">Available colors</h4>
                  <ul
                    role="list"
                    class="mt-auto flex items-center justify-center space-x-3 pt-6"
                  >
                    <li
                      v-for="color in product.availableColors"
                      :key="color.name"
                      class="h-4 w-4 rounded-full border border-black border-opacity-10"
                      :style="{ backgroundColor: color.colorBg }"
                    >
                      <span class="sr-only"> {{ color.name }} </span>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>

          <div class="mt-12 px-4 sm:hidden">
            <a
              href="#"
              class="text-sm font-semibold bg-primary-600 hover:bg-primary-500"
            >
              See everything
              <span aria-hidden="true"> &rarr;</span>
            </a>
          </div>
        </div>
      </section>

      <!-- Sale and testimonials -->
      <div class="relative overflow-hidden">
        <!-- Decorative background image and gradient -->
        <div aria-hidden="true" class="absolute inset-0">
          <div
            class="absolute inset-0 mx-auto max-w-7xl overflow-hidden xl:px-8"
          >
            <img
              src="https://tailwindui.com/img/ecommerce-images/home-page-02-sale-full-width.jpg"
              alt=""
              class="h-full w-full object-cover object-center"
            />
          </div>
          <div class="absolute inset-0 bg-white bg-opacity-75" />
          <div class="absolute inset-0 bg-gradient-to-t from-white via-white" />
        </div>

        <!-- Sale -->
        <section
          aria-labelledby="sale-heading"
          class="relative mx-auto flex max-w-7xl flex-col items-center px-4 pt-32 text-center sm:px-6 lg:px-8"
        >
          <div class="mx-auto max-w-2xl lg:max-w-none">
            <h2
              id="sale-heading"
              class="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl lg:text-6xl"
            >
              Get 25% off during our one-time sale
            </h2>
            <p class="mx-auto mt-4 max-w-xl text-xl text-gray-600">
              Most of our products are limited releases that won't come back.
              Get your favorite items while they're in stock.
            </p>
          </div>
        </section>

        <!-- Testimonials -->
        <section
          aria-labelledby="testimonial-heading"
          class="relative mx-auto max-w-7xl py-24 px-4 sm:px-6 lg:py-32 lg:px-8"
        >
          <div class="mx-auto max-w-2xl lg:max-w-none">
            <h2
              id="testimonial-heading"
              class="text-2xl font-bold tracking-tight text-gray-900"
            >
              What are people saying?
            </h2>

            <div
              class="mt-16 space-y-16 lg:grid lg:grid-cols-3 lg:gap-x-8 lg:space-y-0"
            >
              <blockquote
                v-for="testimonial in testimonials"
                :key="testimonial.id"
                class="sm:flex lg:block"
              >
                <svg
                  width="24"
                  height="18"
                  viewBox="0 0 24 18"
                  xmlns="http://www.w3.org/2000/svg"
                  aria-hidden="true"
                  class="flex-shrink-0 text-gray-300"
                >
                  <path
                    d="M0 18h8.7v-5.555c-.024-3.906 1.113-6.841 2.892-9.68L6.452 0C3.188 2.644-.026 7.86 0 12.469V18zm12.408 0h8.7v-5.555C21.083 8.539 22.22 5.604 24 2.765L18.859 0c-3.263 2.644-6.476 7.86-6.451 12.469V18z"
                    fill="currentColor"
                  />
                </svg>
                <div class="mt-8 sm:mt-0 sm:ml-6 lg:mt-10 lg:ml-0">
                  <p class="text-lg text-gray-600">{{ testimonial.quote }}</p>
                  <cite
                    class="mt-4 block font-semibold not-italic text-gray-900"
                    >{{ testimonial.attribution }}</cite
                  >
                </div>
              </blockquote>
            </div>
          </div>
        </section>
      </div>
    </main>

    <footer aria-labelledby="footer-heading" class="bg-white">
      <h2 id="footer-heading" class="sr-only">Footer</h2>
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="border-t border-gray-200">
          <div class="lg:grid lg:grid-cols-2 lg:gap-x-6 xl:gap-x-8">
            <div class="flex items-center rounded-lg bg-gray-100 p-6 sm:p-10">
              <div class="mx-auto max-w-sm">
                <h3 class="font-semibold text-gray-900">
                  Sign up for our newsletter
                </h3>
                <p class="mt-2 text-sm text-gray-500">
                  The latest news, articles, and resources, sent to your inbox
                  weekly.
                </p>
                <div class="mt-4 sm:mt-6 sm:flex">
                  <label for="email-address" class="sr-only"
                    >Email address</label
                  >
                  <input
                    id="email-address"
                    type="text"
                    v-model="newsLetterInput.value"
                    autocomplete="email"
                    class="w-full min-w-0 appearance-none rounded-md border border-gray-300 bg-white py-2 px-4 text-base text-gray-900 placeholder-gray-500 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500"
                  />
                  <div class="mt-3 sm:mt-0 sm:ml-4 sm:flex-shrink-0">
                    <button
                      class="flex w-full items-center justify-center rounded-md border border-transparent bg-primary-600 py-2 px-4 text-base font-medium text-white shadow-sm hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-white"
                      @click="submitInput"
                    >
                      <LoadingIcon
                        v-if="loading"
                        class="-ml-1 mr-3 h-5 w-5 text-white"
                      />
                      <slot />

                      Sign up
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <div
              class="relative mt-6 flex items-center py-12 px-6 sm:py-16 sm:px-10 lg:mt-0"
            >
              <div class="absolute inset-0 overflow-hidden rounded-lg">
                <img
                  src="https://tailwindui.com/img/ecommerce-images/footer-02-exclusive-sale.jpg"
                  alt=""
                  class="h-full w-full object-cover object-center saturate-0 filter"
                />
                <div class="absolute inset-0 bg-primary-600 bg-opacity-90" />
              </div>
              <div class="relative mx-auto max-w-sm text-center">
                <h3 class="text-2xl font-bold tracking-tight text-white">
                  Get early access
                </h3>
                <p class="mt-2 text-gray-200">
                  Did you sign up to the newsletter? If so, use the keyword we
                  sent you to get access.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- RESULT Frame -->
        <ResultFrame
          :result="result"
          :isInputVulnerable="isInputVulnerable"
          :showComponent="showComponent"
          :flagFound="flagFound"
          :flag="flag"
        ></ResultFrame>

        <div class="py-10 md:flex md:items-center md:justify-between">
          <div class="text-center md:text-left">
            <p class="text-sm text-gray-500">Images provided by Ugmonk</p>
          </div>

          <div class="mt-4 flex items-center justify-center md:mt-0">
            <div class="flex space-x-8">
              <a
                v-for="item in footerNavigation.bottomLinks"
                :key="item.name"
                :href="item.href"
                class="text-sm text-gray-500 hover:text-gray-600"
                >{{ item.name }}</a
              >
            </div>

            <div class="ml-6 border-l border-gray-200 pl-6">
              <a
                href="#"
                class="flex items-center text-gray-500 hover:text-gray-600"
              >
                <img
                  src="https://tailwindui.com/img/flags/flag-canada.svg"
                  alt=""
                  class="h-auto w-5 flex-shrink-0"
                />
                <span class="ml-3 text-sm">Change</span>
                <span class="sr-only">location and currency</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>
<script setup lang="ts">
import { useShopStore } from '@/store/shop'
import { ref } from 'vue'
import ResultFrame from '@/components/ResultFrame.vue'
import useFlagMethods from '@/composables/useFlagMethods'
import LoadingIcon from '@/components/LoadingIcon.vue'

const shopStore = useShopStore()
const showComponent = ref(false)
const loading = ref(false)

const newsLetterInput = ref({
  id: '1',
  value: ''
})

const isInputVulnerable = ref(
  shopStore.isInputVulnerable(newsLetterInput.value.id)
)

// Composable to import vulnerable logic to call flag. getFlag method is called dynamically it is not used nowhere in code
const { result, flagFound, flag, getFlag } = useFlagMethods()

// Method to process input in store
function submitInput() {
  loading.value = true

  result.value = null
  showComponent.value = false

  setTimeout(() => {
    result.value = shopStore.processValue(newsLetterInput.value)
    showComponent.value = true
  }, 1000)
  loading.value = false
}

// Mocked data variables
const offers = [
  {
    name: 'Download the app',
    description: 'Get an exclusive $5 off code',
    href: '#'
  },
  {
    name: "Return when you're ready",
    description: '60 days of free returns',
    href: '#'
  },
  {
    name: 'Sign up for our newsletter',
    description: '15% off your first order',
    href: '#'
  }
]
const trendingProducts = shopStore.produtItems
const collections = [
  {
    name: 'Desk and Office',
    description: 'Work from home accessories',
    imageSrc:
      'https://tailwindui.com/img/ecommerce-images/home-page-02-edition-01.jpg',
    imageAlt:
      'Desk with leather desk pad, walnut desk organizer, wireless keyboard and mouse, and porcelain mug.',
    href: '#'
  },
  {
    name: 'Self-Improvement',
    description: 'Journals and note-taking',
    imageSrc:
      'https://tailwindui.com/img/ecommerce-images/home-page-02-edition-02.jpg',
    imageAlt:
      'Wood table with porcelain mug, leather journal, brass pen, leather key ring, and a houseplant.',
    href: '#'
  },
  {
    name: 'Travel',
    description: 'Daily commute essentials',
    imageSrc:
      'https://tailwindui.com/img/ecommerce-images/home-page-02-edition-03.jpg',
    imageAlt: 'Collection of four insulated travel bottles on wooden shelf.',
    href: '#'
  }
]
const testimonials = [
  {
    id: 1,
    quote:
      "I recently made a purchase from this e-shop for office supplies and I must say, I'm thoroughly impressed! The website is easy to navigate and the checkout process was seamless. The products I received were of high quality and exactly what I was looking for. I would definitely recommend this e-shop to anyone in need of office supplies. 5 stars!",
    attribution: 'Sarah'
  },
  {
    id: 2,
    quote:
      'I was a little hesitant to order office supplies online, but this e-shop exceeded my expectations. The prices were competitive and the delivery was fast. I also appreciated the clear descriptions and product photos on the website, which made it easy to find exactly what I needed. I would definitely use this e-shop again in the future.',
    attribution: 'David'
  },
  {
    id: 3,
    quote:
      "I've had mixed experiences with online shopping in the past, but this e-shop has been a pleasant surprise. The selection of office supplies is vast and the prices are reasonable. I also appreciated the quick response from customer service when I had a question about a product. Overall, I'm very happy with my purchase and would recommend this e-shop to anyone looking for office supplies.",
    attribution: 'Emily'
  }
]
const footerNavigation = {
  products: [
    { name: 'Bags', href: '#' },
    { name: 'Tees', href: '#' },
    { name: 'Objects', href: '#' },
    { name: 'Home Goods', href: '#' },
    { name: 'Accessories', href: '#' }
  ],
  customerService: [
    { name: 'Contact', href: '#' },
    { name: 'Shipping', href: '#' },
    { name: 'Returns', href: '#' },
    { name: 'Warranty', href: '#' },
    { name: 'Secure Payments', href: '#' },
    { name: 'FAQ', href: '#' },
    { name: 'Find a store', href: '#' }
  ],
  company: [
    { name: 'Who we are', href: '#' },
    { name: 'Sustainability', href: '#' },
    { name: 'Press', href: '#' },
    { name: 'Careers', href: '#' },
    { name: 'Terms & Conditions', href: '#' },
    { name: 'Privacy', href: '#' }
  ],
  legal: [
    { name: 'Terms of Service', href: '#' },
    { name: 'Return Policy', href: '#' },
    { name: 'Privacy Policy', href: '#' },
    { name: 'Shipping Policy', href: '#' }
  ],
  bottomLinks: [
    { name: 'Accessibility', href: '#' },
    { name: 'Privacy', href: '#' },
    { name: 'Terms', href: '#' }
  ]
}
</script>
