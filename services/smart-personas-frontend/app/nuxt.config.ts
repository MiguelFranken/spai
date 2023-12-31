// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  css: [
    '~/assets/main.css',
    '@unocss/reset/tailwind.css',
  ],
  components: {
    dirs: [
      '~/components',
    ],
  },
  imports: {
    dirs: ['stores'],
  },
  modules: [
    [
      '@pinia/nuxt',
      {
        autoImports: ['defineStore', 'acceptHMRUpdate'],
      },
    ],
    '@nuxt/devtools',
    '@unocss/nuxt',
    '@vueuse/nuxt',
    '@vue-macros/nuxt',
    'nuxt-vitest',
  ],
  routeRules: {
    '/**': {
      headers: {
        'cache-control': 's-maxage=300, maxage=300, type=public, stale-while-revalidate=90000, stale-if-error=90000',
      },
    },
  },
  typescript: {
    shim: false,
  },
  vite: {
    resolve: {
      preserveSymlinks: true,
    },
  },
  runtimeConfig: {
    public: {
      mockEnabled: !!process.env.NUXT_SHOULD_MOCK_REVIEW_GENERATOR_API || false,
    },
  },
})
