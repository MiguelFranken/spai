<script setup lang="ts">
const route = useRoute()
const url = (Array.isArray(route) ? route[0] : route).params.url

definePageMeta({
  layout: 'content',
  validate: async (route) => {
    try {
      // eslint-disable-next-line no-new
      new URL((Array.isArray(route) ? route[0] : route).params.url)
      return true
    } catch (e) {
      return false
    }
  }
})


const {pending, data, error} = useFetch(
  `http://review-generator.local/review?url=${encodeURIComponent(url)}`,
  //`http://review-generator.local/?url=${encodeURIComponent(url)}`,
  {
    lazy: true,
  }
)
</script>

<template>
  <div>
    <div v-if="pending" class="h-screen flex items-center justify-center">
      <div class="flex flex-col items-center gap-4">
        <LoadingSpinner/>
        <div>Loading Accessibility Review</div>
      </div>
    </div>
    <div v-else-if="error">
      ERROR: {{error}}
    </div>
    <Review class="pt-16" v-else :review="data.review" />
  </div>
</template>