<template>
  <div class="w-full py-12 bg-gray-800 color-white">
    <LayoutContainer>
      <div class="flex justify-between">
        <!-- Persona -->
        <div class="flex gap-8">
          <div>
            <div class="relative inline-block">
              <img
                class="h-24 w-24 rounded-full"
                src="https://thispersondoesnotexist.com/"
                alt=""
              />
            </div>
          </div>

          <div>
            <div class="text-3xl">Claudia</div>
            <ul>
              <li>Grandmother with macular degeneration</li>
              <li>Uses a screen magnifier and changes colors for contrast</li>
              <li>Volunteers in social work</li>
            </ul>
          </div>
        </div>

        <div class="flex gap-8">
          <div>
            <img
              class="h-24 w-24 rounded-full"
              src="https://randomuser.me/api/portraits/women/1.jpg"
              alt=""
            />
            <div class="text-center">John</div>
          </div>

          <div>
            <img
              class="h-24 w-24 rounded-full"
              src="https://randomuser.me/api/portraits/men/2.jpg"
              alt=""
            />
            <div class="text-center">John</div>
          </div>
        </div>
      </div>
    </LayoutContainer>
  </div>
</template>
