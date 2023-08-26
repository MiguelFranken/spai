<script setup lang="ts">
import backgroundImagePath from '~/assets/grandma.png'

defineProps<{
  name: string
  url: string
  isLoading: boolean
}>()
</script>

<template>
  <div
    class="relative w-full color-white overflow-hidden"
  >
    <div class="absolute inset-0 overflow-hidden">
      <div
        class="w-full h-128 bg-cover bg-center blur-lg !bg-fixed"
        :style="{ background: `linear-gradient(to right bottom, rgba(71, 253, 220, 0.77), rgba(11, 105, 245, 0.49)), url(${backgroundImagePath})` }"
      />
    </div>

    <div class="py-12">
      <LayoutContainer class="relative">
        <div class="flex justify-between">
          <!-- Persona -->
          <div class="flex gap-8 items-center">
            <div>
              <div class="relative inline-block">
                <img
                  class="h-40 w-40 rounded-full"
                  :src="backgroundImagePath"
                  alt=""
                >
              </div>
            </div>

            <div class="space-y-2">
              <div class="text-4xl font-pacifico">
                {{ name }}
              </div>
              <ul class="list-disc list-inside">
                <li>Grandmother with macular degeneration</li>
                <li>Uses a screen magnifier and changes colors for contrast</li>
                <li>Volunteers in social work</li>
              </ul>
            </div>
          </div>

          <div class="flex gap-8 items-center">
            <Avatar :src="backgroundImagePath" name="Claudia" />
            <Avatar :src="backgroundImagePath" name="Claudia" />
          </div>
        </div>
      </LayoutContainer>
    </div>

    <div
      class="relative h-12 bg-black/10 test"
      :class="{
        'before:(absolute inset-0 animate-shimmer animate-[shimmer_1.5s_infinite] bg-gradient-to-r from-transparent via-black/10 to-transparent content-empty)': isLoading,
      }"
    >
      <LayoutContainer class="h-full flex items-center">
        <ClientOnly>
          Reviewing Website: {{ url }}
        </ClientOnly>
      </LayoutContainer>
    </div>
  </div>
</template>
