<script setup lang="ts">
interface Props {
  review: string
}
const { review } = defineProps<Props>()

const paragraphs = computed(() => review.split("\n\n"))

function splitParagraph(paragraph: string): [string, string] {
  const regex = /([^.?]+[.?])/;  // Match up to the first period or question mark
  const match = paragraph.match(regex);

  if (match) {
    const firstSentence = match[1].trim();
    const rest = paragraph.substring(firstSentence.length).trim();
    return [firstSentence, rest];
  } else {
    // Return the whole paragraph as the first sentence if no punctuation found
    return [paragraph, ""];
  }
}

const splittedParagraphs = computed(() => paragraphs.value.map(splitParagraph))
</script>

<template>
  <div class="py-32">
    <div class="flex flex-col gap-16">
      <section v-for="paragraph in splittedParagraphs" class="space-y-2">
        <h2 class="font-bold text-4xl">{{ paragraph[0] }}</h2>
        <p>{{ paragraph[1] }}</p>
      </section>
    </div>
  </div>
</template>
