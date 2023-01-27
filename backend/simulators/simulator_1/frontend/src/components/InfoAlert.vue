<template>
  <div class="rounded-md bg-blue-50 p-4">
    <div>
      <div class="flex-shrink-0 flex items-center">
        <InformationCircleIcon
          class="h-5 w-5 text-blue-400"
          aria-hidden="true"
        />
        <span class="text-base text-blue-400 font-bold font-sans ml-3">
          Results</span
        >
      </div>
      <div v-if="content.results" class="ml-3 flex-1 md:flex flex-col">
        <div
          v-for="(result, idx) in content.results"
          :key="idx"
          class="text-sm text-blue-400 py-2"
        >
          <span class="text-sm text-blue-700 font-sans font-bold"> Response: {{ idx }}</span>
          <pre class="text-blue-700">
          {{ result.response }}

          </pre>
        </div>
      </div>
      <div v-else class="ml-3 flex-1 md:flex md:justify-between">
        <p class="text-sm text-blue-700">Results will be showed here</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { InformationCircleIcon } from '@heroicons/vue/20/solid'

const props = defineProps({
  content: {
    type: Object,
    required: true
  }
})
</script>
