<script setup lang="ts">
const url = ref('');
const review = ref('');
const error = ref('');

const fetchReview = async () => {
  try {
    const response = await fetch(
      //`http://review-generator.local/review?url=${url.value}`,
      `http://localhost:3000/a11y-report?url=http://example.com`,
    );
    if (response.ok) {
      const data = await response.json();
      console.log("data", data)
      review.value = data.review;
      error.value = '';
    } else {
      error.value = 'Failed to generate review. Please try again later.';
      console.error('Failed to generate review. Please try again later.')
      review.value = '';
    }
  } catch (e) {
    error.value = 'An error occurred while fetching the review!';
    console.error(e)
    review.value = '';
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
    <div class="p-8 bg-white rounded-lg shadow-md w-96">
      <h1 class="text-2xl font-semibold mb-4 text-blue-500">Accessibility Review</h1>

      <div class="flex flex-col space-y-4">
        <input
          v-model="url"
          type="text"
          placeholder="Enter URL"
          class="p-2 border rounded"
        />

        <button
          @click="fetchReview"
          class="border-0 p-2 bg-blue-500 text-white rounded hover:bg-blue-600 cursor-pointer"
        >
          Generate Review
        </button>

        <div v-if="review" class="text-green-500">
          {{ review }}
        </div>
        <div v-if="error" class="text-red-500">
          {{ error }}
        </div>
      </div>
    </div>
  </div>
</template>
