<template>
  <div class="w-full overflow-y-auto p-4 bg-white">
    <main>
      <!-- Product -->
      <div class="bg-white">
        <div
          class="mx-auto max-w-2xl px-4 pt-16 pb-5 sm:px-6 sm:pt-24 sm:pb-5 lg:grid lg:max-w-7xl lg:grid-cols-2 lg:gap-x-8 lg:px-8"
        >
          <!-- Product details -->
          <div class="lg:max-w-lg lg:self-end">

            <div class="mt-4">
              <h1
                class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl"
              >
                {{ productDetail.name }}
              </h1>
            </div>

            <section aria-labelledby="information-heading" class="mt-4">
              <h2 id="information-heading" class="sr-only">
                Product information
              </h2>

              <div class="flex items-center">
                <p class="text-lg text-gray-900 sm:text-xl">
                  {{ productDetail.price }}
                </p>

                <div class="ml-4 border-l border-gray-300 pl-4">
                  <h2 class="sr-only">Reviews</h2>
                  <div class="flex items-center">
                    <div>
                      <div class="flex items-center">
                        <StarIcon
                          v-for="rating in [0, 1, 2, 3, 4]"
                          :key="rating"
                          :class="[
                            reviews.average > rating
                              ? 'text-yellow-400'
                              : 'text-gray-300',
                            'h-5 w-5 flex-shrink-0'
                          ]"
                          aria-hidden="true"
                        />
                      </div>
                      <p class="sr-only">
                        {{ reviews.average }} out of 5 stars
                      </p>
                    </div>
                    <p class="ml-2 text-sm text-gray-500">
                      {{ reviews.totalCount }} reviews
                    </p>
                  </div>
                </div>
              </div>

              <div class="mt-4 space-y-6">
                <p class="text-base text-gray-500">{{ productDetail.imageAlt }}</p>
              </div>
            </section>
          </div>

          <!-- Product image -->
          <div
            class="mt-10 lg:col-start-2 lg:row-span-2 lg:mt-0 lg:self-center"
          >
            <div class="aspect-w-1 aspect-h-1 overflow-hidden rounded-lg">
              <img
                :src="productDetail.imageSrc"
                :alt="productDetail.imageAlt"
                class="h-full w-full object-cover object-center"
              />
            </div>
          </div>

          <!-- Product form -->
          <div
            class="mt-10 lg:col-start-1 lg:row-start-2 lg:max-w-lg lg:self-start"
          >
            <section aria-labelledby="options-heading">
              <h2 id="options-heading" class="sr-only">Product options</h2>

              <div>
                <div class="mt-10">
                  <button
                    type="submit"
                    :disabled="true"
                    class="flex w-full items-center justify-center rounded-md border border-transparent bg-primary-200 py-3 px-8 text-base font-medium text-white hover:bg-primary-200 focus:outline-none focus:ring-2 focus:ring-primary-200 focus:ring-offset-2 focus:ring-offset-gray-50"
                  >
                    Sold out
                  </button>
                </div>
                <div class="mt-6 text-center">
                  <div class="group inline-flex text-base font-medium">
                    <ShieldCheckIcon
                      class="mr-2 h-6 w-6 flex-shrink-0 text-gray-400 group-hover:text-gray-500"
                      aria-hidden="true"
                    />
                    <span class="text-gray-500 hover:text-gray-700"
                      >Lifetime Guarantee</span
                    >
                  </div>
                </div>
              </div>
            </section>
          </div>
        </div>
      </div>

      <div
        class="mx-auto max-w-2xl px-4 py-5 sm:px-6 sm:py-5 lg:max-w-7xl lg:px-8"
      >
        <!-- Policies section -->
        <section aria-labelledby="policy-heading" class="mt-16 lg:mt-24">
          <h2 id="policy-heading" class="sr-only">Our policies</h2>
          <div
            class="grid grid-cols-1 gap-y-12 sm:grid-cols-2 sm:gap-x-6 lg:grid-cols-4 lg:gap-x-8"
          >
            <div v-for="policy in policies" :key="policy.name">
              <img :src="policy.imageSrc" alt="" class="h-24 w-auto" />
              <h3 class="mt-6 text-base font-medium text-gray-900">
                {{ policy.name }}
              </h3>
              <p class="mt-3 text-base text-gray-500">
                {{ policy.description }}
              </p>
            </div>
          </div>
        </section>
      </div>

      <div aria-labelledby="reviews-heading" class="bg-white">
        <div
          class="mx-auto max-w-2xl py-5 px-4 sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-12 lg:gap-x-8 lg:py-5 lg:px-8"
        >
          <div class="lg:col-span-4">
            <h2
              id="reviews-heading"
              class="text-2xl font-bold tracking-tight text-gray-900"
            >
              Customer Reviews
            </h2>

            <div class="mt-3 flex items-center">
              <div>
                <div class="flex items-center">
                  <StarIcon
                    v-for="rating in [0, 1, 2, 3, 4]"
                    :key="rating"
                    :class="[
                      reviews.average > rating
                        ? 'text-yellow-400'
                        : 'text-gray-300',
                      'flex-shrink-0 h-5 w-5'
                    ]"
                    aria-hidden="true"
                  />
                </div>
                <p class="sr-only">{{ reviews.average }} out of 5 stars</p>
              </div>
              <p class="ml-2 text-sm text-gray-900">
                Based on {{ reviews.totalCount }} reviews
              </p>
            </div>

            <div class="mt-6">
              <h3 class="sr-only">Review data</h3>

              <dl class="space-y-3">
                <div
                  v-for="count in reviews.counts"
                  :key="count.rating"
                  class="flex items-center text-sm"
                >
                  <dt class="flex flex-1 items-center">
                    <p class="w-3 font-medium text-gray-900">
                      {{ count.rating
                      }}<span class="sr-only"> star reviews</span>
                    </p>
                    <div
                      aria-hidden="true"
                      class="ml-1 flex flex-1 items-center"
                    >
                      <StarIcon
                        :class="[
                          count.count > 0 ? 'text-yellow-400' : 'text-gray-300',
                          'flex-shrink-0 h-5 w-5'
                        ]"
                        aria-hidden="true"
                      />

                      <div class="relative ml-3 flex-1">
                        <div
                          class="h-3 rounded-full border border-gray-200 bg-gray-100"
                        />
                        <div
                          v-if="count.count > 0"
                          class="absolute inset-y-0 rounded-full border border-yellow-400 bg-yellow-400"
                          :style="{
                            width: `calc(${count.count} / ${reviews.totalCount} * 100%)`
                          }"
                        />
                      </div>
                    </div>
                  </dt>
                  <dd
                    class="ml-3 w-10 text-right text-sm tabular-nums text-gray-900"
                  >
                    {{ Math.round((count.count / reviews.totalCount) * 100) }}%
                  </dd>
                </div>
              </dl>
            </div>

            <div class="mt-10">
              <h3 class="text-lg font-medium text-gray-900">
                Share your thoughts
              </h3>
              <p class="mt-1 text-sm text-gray-600">
                If you’ve used this product, share your thoughts with other
                customers
              </p>

              <a
                href="#"
                class="mt-6 inline-flex w-full items-center justify-center rounded-md border border-gray-300 bg-white py-2 px-8 text-sm font-medium text-gray-900 hover:bg-gray-50 sm:w-auto lg:w-full"
                >Write a review</a
              >
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>
<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router'
import {
  ShieldCheckIcon,
} from '@heroicons/vue/24/outline'
import {
  StarIcon
} from '@heroicons/vue/20/solid'
import { useShopStore } from '@/store/shop'
import { ref } from 'vue'

const route = useRoute()

const shopStore = useShopStore()
const productDetail: any = ref(
  shopStore.getProductById(Number(route.params.id))
)

const router = useRouter()

const policies = [
  {
    name: 'Free delivery all year long',
    description:
      'Name another place that offers year long free delivery? We’ll be waiting. Order now and you’ll get delivery absolutely free.',
    imageSrc:
      'https://tailwindui.com/img/ecommerce/icons/icon-delivery-light.svg'
  },
  {
    name: '24/7 Customer Support',
    description:
      'Or so we want you to believe. In reality our chat widget is powered by a naive series of if/else statements that churn out canned responses. Guaranteed to irritate.',
    imageSrc: 'https://tailwindui.com/img/ecommerce/icons/icon-chat-light.svg'
  },
  {
    name: 'Fast Shopping Cart',
    description:
      "Look at the cart in that icon, there's never been a faster cart. What does this mean for the actual checkout experience? I don't know.",
    imageSrc:
      'https://tailwindui.com/img/ecommerce/icons/icon-fast-checkout-light.svg'
  },
  {
    name: 'Gift Cards',
    description:
      "We sell these hoping that you will buy them for your friends and they will never actually use it. Free money for us, it's great.",
    imageSrc:
      'https://tailwindui.com/img/ecommerce/icons/icon-gift-card-light.svg'
  }
]

const reviews = {
  average: 4,
  totalCount: 1624,
  counts: [
    { rating: 5, count: 1019 },
    { rating: 4, count: 162 },
    { rating: 3, count: 97 },
    { rating: 2, count: 199 },
    { rating: 1, count: 147 }
  ],
  featured: [
    {
      id: 1,
      rating: 5,
    }
  ]
}
</script>
