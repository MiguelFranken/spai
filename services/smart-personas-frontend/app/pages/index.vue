<script setup lang="ts">
function foo() {
  // eslint-disable-next-line no-console
  console.log('Hello')
}
</script>

<template>
  <div class="bg-color-orange-400 p-8 space-y-6">
    <div
      class="bg-red-500 rounded-$radii-200 p-8"
      outline="~ solid size-$size-100 color-$color-primary-hover-cta-background"
      border="~ solid size-$size-50 color-black"
    >
      Hello World
    </div>

    <button type="button" @click="foo">
      hello world
    </button>
  </div>
</template>
