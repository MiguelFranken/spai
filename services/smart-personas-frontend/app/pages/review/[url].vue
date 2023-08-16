<script setup lang="ts">
const route = useRoute()
const url = (Array.isArray(route) ? route[0] : route).params.url

definePageMeta({
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
    <div v-else class="pt-16">
      <div class="sm:flex sm:items-center sm:justify-between pb-4">
        <div class="flex flex-col gap-0.5">
          <h3 class="text-md font-semibold leading-6 text-gray-900 my-0">Accessibility Report</h3>
          <a :href="url" class="my-0 max-w-2xl text-sm text-blue">{{ url }}</a>
        </div>
        <div class="mt-3 flex sm:ml-4 sm:mt-0">
          <NuxtLink to="/" class="no-underline border-0 cursor-pointer inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Back</NuxtLink>
        </div>
      </div>

      <section class="relative isolate overflow-hidden bg-white rounded-md ring-1 ring-inset ring-gray-200 shadow-sm">
        <div class="w-full">
          <figure class="mt-10 mx-0">
            <figcaption class="mt-10">
              <div class="w-full flex justify-center">
                <img
                  class="h-48 w-48 rounded-full"
                  src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                  alt=""
                />  
              </div>
              
              <div class="mt-4 flex items-center justify-center space-x-3 text-base">
                <div class="font-semibold text-gray-900">Claudia</div>
                <svg viewBox="0 0 2 2" width="3" height="3" aria-hidden="true" class="fill-gray-900">
                  <circle cx="1" cy="1" r="1" />
                </svg>
                <div class="text-gray-600">Social Worker</div>
              </div>
            </figcaption>

            <blockquote class="text-center text-xl font-semibold leading-8 text-gray-900 sm:text-2xl sm:leading-9">
              <p>"QUOTE"</p>
            </blockquote>
            
            <p class="p-8 text-justify">{{ data.review }}</p>
          </figure>
        </div>
      </section>
    </div>
  </div>
</template>