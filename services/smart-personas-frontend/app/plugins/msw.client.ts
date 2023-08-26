export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.hook('app:beforeMount', async () => {
    const config = useRuntimeConfig()
    const isMockEnabled = config.public.mockEnabled

    if (isMockEnabled && process.client) {
      const baseUrl = 'http://review-generator.smart-personas.local'

      async function startWorker() {
        const msw = await import('msw')
        const mswBrowser = await import('msw/browser')

        const handlers = [
          msw.http.get(`${baseUrl}/review`, () => {
            const review = 'Oh, Musikhaus Thomann, where do I begin? First, hats off for being Europe’s largest music house. Truly, I had high hopes as I embarked on this digital exploration. My journey began long before my vision decided to play peekaboo, and music has been a beloved part of that. Who doesn\'t love the soothing notes of a piano or the hum of a guitar? I dreamt of treating my niece to a new violin, perhaps serenading my next family gathering.\n'
              + '\n'
              + 'However, diving into your site felt like trying to navigate one of those newfangled, overly-complicated sheet music pieces. Take, for instance, the unexpected roles you’ve assigned to elements. Imagine handing me a tambourine when I asked for a trumpet. That\'s how it felt. And those unlabeled buttons? It’s like trying to play a tune without knowing the notes. Ah, and the color contrast – or should I say, the lack thereof? It was akin to attempting to read lyrics written in invisible ink. I often share with my clients the importance of clarity, especially in the challenges they face. Your website felt like a mystery novel where all the critical pages were torn out.\n'
              + '\n'
              + 'Speaking of mysteries, those images without descriptions were like going to a concert blindfolded. I\'m all for surprises, but this was next-level. And, oh! The repeated alternative text reminded me of the time I accidentally played the same song on repeat at a community gathering. Once, okay. Twice, oops! But constantly? That\'s a party foul. Lastly, the lack of organized sections felt like attending a music festival with no signs pointing to the stages. Where\'s the main act? The food stalls? The exits? Who knows! My dear Thomann, your website is a symphony, but it seems some instruments are out of tune. I hope this review strikes a chord and inspires a harmonious change. Until then, I\'ll be humming along elsewhere, searching for that perfect violin. 🎻🎵😉'

            return msw.HttpResponse.json({ review })
          }),
        ]

        const worker = mswBrowser.setupWorker(...handlers)
        await worker.start({
          onUnhandledRequest: ({ url }, print) => {
            if (url.startsWith(baseUrl))
              print.warning()
          },
        })
      }

      await startWorker()
    }
  })
})
