<script setup lang="ts">
const { name } = defineProps<{
  name: string
  src: string
}>()
</script>

<template>
  <div class="space-y-1">
    <div class="relative h-24 w-24 rounded-full bg-sky-700">
      <img
        class="w-full h-full rounded-full opacity-50"
        :src="src"
        alt=""
      >

      <div class="absolute inset-0 flex items-center text-center color-gray-300 leading-none">
        Coming Soon
      </div>
    </div>

    <div class="text-center">
      {{ name }}
    </div>
  </div>
</template>
