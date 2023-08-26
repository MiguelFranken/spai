<script setup lang="ts">
const route = useRoute()
const url = (Array.isArray(route) ? route[0] : route).params.url

const reviewURL = useReviewURL()
reviewURL.value = url

const isLoadingReview = useIsLoadingReview()
isLoadingReview.value = true

definePageMeta({
  layout: 'content',
  validate: async (route) => {
    try {
      // eslint-disable-next-line no-new
      new URL((Array.isArray(route) ? route[0] : route).params.url)
      return true
    }
    catch (e) {
      return false
    }
  },
})

interface ReviewResponse {
  review: string
}

const { pending, data, error } = useFetch<ReviewResponse>(
  `http://review-generator.smart-personas.local/review?url=${encodeURIComponent(url)}`,
  // `http://review-generator.local/?url=${encodeURIComponent(url)}`,
  {
    server: false,
    lazy: true,
  },
)

watch(pending, () => isLoadingReview.value = false)
</script>

<template>
  <div>
    <div v-if="pending" class="flex items-center justify-center">
      <div class="flex flex-col items-center gap-4 pt-8">
        <LoadingSpinner />
        <div>Loading Accessibility Review</div>
      </div>
    </div>
    <div v-else-if="error">
      ERROR: {{ error }}
    </div>
    <Review v-else-if="data" class="pt-16" :review="data.review" />
  </div>
</template>
