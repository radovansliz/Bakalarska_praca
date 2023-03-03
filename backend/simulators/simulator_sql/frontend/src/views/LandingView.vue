<template>
  <div class="w-full overflow-y-auto p-4 bg-dark-400">

    <!-- Instructions -->
      <div class="rounded-md bg-yellow-50 p-4">
        <div class="flex">
          <div class="flex-shrink-0">
            <InformationCircleIcon
              class="h-5 w-5 text-yellow-400"
              aria-hidden="true"
            />
          </div>
          <div class="ml-3 flex-1 font-bold">
            <p class="text-base text-yellow-700">
              1. Nájdite SQL zraniteľnosť webovej aplikácie
            </p>
            <p class="text-base text-yellow-700">
              2. Využite zraniteľnosť a nájdite v databáze tabulku s ukrytým flagom
            </p>
            <p class="text-base text-yellow-700">
              3. Prezentujte nájdený výsledok - FLAG
            </p>
          </div>
        </div>
      </div>

    <div class="w-full py-5 text-3xl text-white font-bold">
      Welcome to CTF Bank
    </div>
    <div class="w-full py-5">
      <img
        alt=""
        class="w-full object-cover max-h-60 rounded-md"
        src="@/assets/images/accountant-calculating-profit-with-financial-analysis-graphs_74855-4937.webp"
      />
    </div>
    <div class="py-4 text-gray-100 text-base font-sans">
      <p>
        As a community-focused bank, we pride ourselves on delivering
        personalized service and customized solutions to meet the unique needs
        of our customers.
      </p>
      <p>
        We offer a wide range of banking products and services, including
        checking and savings accounts, mortgages, business loans, and investment
        options.
      </p>
      <p>
        Our team of dedicated professionals is here to help you every step of
        the way, whether you're just starting out, growing your business, or
        planning for retirement.
      </p>
      <p>
        We believe in building long-lasting relationships and being there for
        our customers when they need us most. At CTF Bank, we are
        committed to the well-being of our customers and our communities. We
        strive to be a responsible corporate citizen and make a positive impact
        wherever we do business.
      </p>
    </div>
    <div class="py-4">
      <div class="w-full">
        <div class="w-full mb-5">
          <h3 class="text-2xl font-medium leading-6 text-white">
            Exchange rate
          </h3>
          <p class="mt-1 max-w-2xl text-sm text-gray-50">
            End-of-day prices are provided by Europe Central bank. All prices
            are compared with Euro.
          </p>
        </div>
        <h3 class="text-xl font-bold leading-6 text-gray-50">BUY</h3>
        <dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-3">
          <MoneyStatWidget
            v-for="item in stats"
            :key="item.title"
            :value="item.value"
            :image="item.image"
            :title="item.title"
            :bg="'dark-500'"
            :color="'white'"
          ></MoneyStatWidget>
        </dl>
      </div>
      <h3 class="text-xl font-bold leading-6 text-gray-50 mt-10">SELL</h3>
      <dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-3">
        <MoneyStatWidget
          v-for="item in exchangeSell"
          :key="item.title"
          :value="item.value"
          :image="item.image"
          :title="item.title"
          :bg="'dark-500'"
          :color="'white'"
        ></MoneyStatWidget>
      </dl>
    </div>
    <div class="w-full">
      <NewsLetterPanel></NewsLetterPanel>
    </div>
  </div>
</template>
<script setup lang="ts">
import MoneyStatWidget from '@/components/MoneyStatWidget.vue'
import NewsLetterPanel from '@/components/NewsLetterPanel.vue'
import { InformationCircleIcon } from '@heroicons/vue/20/solid'


const stats = [
  { title: 'USD', value: '1.0844', image: 'usa' },
  { title: 'CZK', value: '25.2150', image: 'cz' },
  { title: 'GBP', value: '0.8964', image: 'uk' }
]

const exchangeSell = [
  { title: 'USD', value: '1.0110', image: 'usa' },
  { title: 'CZK', value: '23.5090', image: 'cz' },
  { title: 'GBP', value: '0.8192', image: 'uk' }
]
</script>
