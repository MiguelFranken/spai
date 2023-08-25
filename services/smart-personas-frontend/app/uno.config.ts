// uno.config.ts
import { defineConfig, presetAttributify, presetUno, presetIcons, presetWebFonts } from 'unocss'

export default defineConfig({
  presets: [
    presetUno(),
    presetAttributify(),
    presetIcons({
      scale: 1.2,
    }),
    presetWebFonts({
      provider: 'google',
      fonts: {
        pacifico: 'Pacifico',
      },
    })
  ],
})
