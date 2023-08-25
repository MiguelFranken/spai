<script setup lang="ts">
const url = ref('');

const isValidURL = computed(() => {
  try {
    // eslint-disable-next-line no-new
    new URL(url.value)
    return true
  } catch (e) {
    return false
  }
})

const reviewPage = computed(() => `/review/${encodeURIComponent(url.value)}`)
</script>

<template>
  <div class="pt-32 flex items-center justify-center">
    <div class="p-8 bg-white rounded-lg shadow-md w-96">
      <h1 class="text-2xl font-semibold mb-4 text-blue-500">Accessibility Reviews</h1>

      <div class="flex flex-col space-y-4">
        <input
          v-model="url"
          type="text"
          placeholder="Enter URL"
          class="p-2 border rounded"
        />

        <NuxtLink
          :to="isValidURL ? reviewPage : undefined"
          class="border-0 text-center p-2 text-white rounded"
          :class="{
            'cursor-pointer bg-blue-500 hover:bg-blue-600': isValidURL,
            'cursor-not-allowed bg-gray-300': !isValidURL
          }"
        >
          Generate Review
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
