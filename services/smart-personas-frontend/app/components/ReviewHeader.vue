<template>
  <div class="w-full py-12 bg-yellow-400 color-white">
    <LayoutContainer>
      <div class="flex justify-between">
        <!-- Persona -->
        <div class="flex gap-8 items-center">
          <div>
            <div class="relative inline-block">
              <img
                class="h-40 w-40 rounded-full"
                src="~/assets/grandma.png"
                alt=""
              />
            </div>
          </div>
          
          <div class="space-y-4">
            <div class="text-4xl font-bold">Claudia</div>
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
            />
            <div class="text-center">John</div>
          </div>

          <div>
            <img
              class="h-24 w-24 rounded-full"
              src="~/assets/grandma.png"
              alt=""
            />
            <div class="text-center">John</div>
          </div>
        </div>
      </div>
    </LayoutContainer>
  </div>
</template>
