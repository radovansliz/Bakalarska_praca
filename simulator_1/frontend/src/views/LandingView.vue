<template>
  <div class="w-full p-4 bg-dark-400">
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
  </div>
</template>
<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router'
import MoneyStatWidget from '@/components/MoneyStatWidget.vue'

const router = useRouter()
const route = useRoute()

const goBack = () => {
  router.go(-1)
}

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
