<script setup lang="ts">
interface Props {
  review: string
}
const { review } = defineProps<Props>()

const paragraphs = computed(() => review.split("\n\n"))

function splitParagraph(paragraph: string): string {
  const splitNum = 8

  return [paragraph.split(' ').slice(0, splitNum).join(' '), paragraph.split(' ').slice(splitNum).join(' ')];
}

const splittedParagraphs = computed(() => paragraphs.value.map(splitParagraph))
</script>

<template>
  <div class="py-32">
    <ul class="flex flex-col gap-16">
      <li v-for="paragraph in splittedParagraphs">
        <span class="font-bold text-4xl">{{ paragraph[0] }}</span>
        <span>{{ paragraph[1] }}</span>
      </li>
    </ul>
  </div>
</template>
