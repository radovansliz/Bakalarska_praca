<template>
  <div class="w-full overflow-y-auto p-4 bg-dark-400">
    <div class="flex items-center justify-center text-white text-4xl font-bold">
      Coming soon
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
