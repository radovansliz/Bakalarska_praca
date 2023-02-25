<template>
  <div
    v-if="result"
    class="w-full p-5 border-primary-800 border-2 mt-5 rounded-md"
  >
    <div class="flex-shrink-0 flex items-center mb-2">
      <InformationCircleIcon class="h-5 w-5 text-blue-400" aria-hidden="true" />
      <span class="full text-xl font-bold text-gray-600 ml-2">
        Result of input
      </span>
    </div>

    <h3 class="font-bold text-gray-600 mb-3">Here is your result:</h3>

    <div v-if="!isInputVulnerable && showComponent" class="font-bold text-lg">
      {{ result }}
    </div>
    <div
      v-else
      v-html="result"
      class="font-bold text-xl text-primary-600"
    ></div>
    <div
      v-if="flagFound"
      class="w-full flex items-center justify-center font-bold text-2xl p-4"
    >
      {{ flag }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { InformationCircleIcon } from '@heroicons/vue/20/solid'

const props = defineProps({
  result: {
    required: true
  },
  flag: {
    type: String,
    required: true
  },
  flagFound: {
    type: Boolean,
    required: true
  },
  isInputVulnerable: {
    type: Boolean,
    required: true
  },
  showComponent: {
    type: Boolean,
    required: true
  }
})
</script>
