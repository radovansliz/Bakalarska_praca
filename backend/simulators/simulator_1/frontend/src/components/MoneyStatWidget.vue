<template>
  <div
    :class="'bg-' + props.bg"
    class="overflow-hidden rounded-lg px-4 py-5 shadow sm:p-6"
  >
    <div class="w-full flex">
      <div class="mr-3">
        <img
          v-if="image === 'usa'"
          alt=""
          style="width: 20px; height: 20px"
          src="@/assets/images/usa.svg"
        />
        <img
          v-if="image === 'uk'"
          alt=""
          style="width: 20px; height: 20px"
          src="@/assets/images/uk.svg"
        />
        <img
          v-if="image === 'cz'"
          alt=""
          style="width: 20px; height: 20px"
          src="@/assets/images/cz.svg"
        />
      </div>
      <dt :class="'text-' + color" class="truncate text-sm font-medium">
        {{ props.title }}
      </dt>
    </div>
    <dd
      :class="'text-' + color"
      class="mt-1 text-3xl font-semibold tracking-tight"
    >
      {{ props.value }}
    </dd>
  </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router'
import { isNumber } from '@vueuse/core'

const router = useRouter()
const goBack = () => {
  router.go(-1)
}

const props = defineProps({
  image: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  },
  value: {
    type: String,
    required: true
  },
  bg: {
    type: String,
    required: false,
    default: 'white'
  },
  color: {
    type: String,
    required: false,
    default: 'black'
  }
})
</script>
