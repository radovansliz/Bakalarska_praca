<template>
  <div class="w-full flex flex-col h-full min-h-screen">
    <!-- SIDEBAR -->
    <AppNavbar></AppNavbar>
    <!-- MAIN CONTENT -->
    <div class="flex h-full min-w-[0] overflow-hidden bg-gray-50 relative">
      <RouterView v-slot="{ Component }">
        <transition
          id="transitionParent"
          name="route"
          mode="out-in"
          :style="{
            '--transition-duration': routeTransitionDuration + 'ms'
          }"
        >
          <component
            :is="Component"
            :key="
              route.meta.componentKey
                ? route.meta.componentKey(route)
                : route.name
            "
          />
        </transition>
      </RouterView>
    </div>
  </div>
</template>
<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router'
import AppNavbar from '@/layout/app/AppNavbar.vue'
const route = useRoute()
const routeTransitionDuration = 150 // in miliseconds
</script>
