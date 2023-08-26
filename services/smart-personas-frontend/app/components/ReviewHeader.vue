<script setup lang="ts">
</script>

<template>
  <div
    class="relative w-full color-white overflow-hidden"
  >
    <div class="absolute inset-0 overflow-hidden">
      <div
        class="w-full h-128 container-background bg-cover bg-center blur-lg !bg-fixed"
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
                  src="~/assets/grandma.png"
                  alt=""
                >
              </div>
            </div>

            <div class="space-y-2">
              <div class="text-4xl font-pacifico">
                Claudia
              </div>
              <ul class="list-disc list-inside">
                <li>Grandmother with macular degeneration</li>
                <li>Uses a screen magnifier and changes colors for contrast</li>
                <li>Volunteers in social work</li>
              </ul>
            </div>
          </div>

          <div class="flex gap-8 items-center">
            <div>
              <img
                class="h-24 w-24 rounded-full"
                src="~/assets/grandma.png"
                alt=""
              >
              <div class="text-center">
                John
              </div>
            </div>

            <div>
              <img
                class="h-24 w-24 rounded-full"
                src="~/assets/grandma.png"
                alt=""
              >
              <div class="text-center">
                John
              </div>
            </div>
          </div>
        </div>
      </LayoutContainer>
    </div>

    <div class="relative bg-black/10 h-12">
      <LayoutContainer class="h-full flex items-center">
        Reviewing website: https://thomann.de/
      </LayoutContainer>
    </div>
  </div>
</template>

<style scoped>
.container-background {
  background: linear-gradient(to right bottom, rgba(71, 253, 220, 0.77), rgba(11, 105, 245, 0.49)), url('/_nuxt/assets/grandma.png');
}
</style>
