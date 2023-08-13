import { writeFile } from 'node:fs'
import puppeteer from 'puppeteer'

import { loadPage } from '@axe-core/puppeteer'
import type { AxeResults } from 'axe-core'

interface FilteredResult {
  help: string
  impact: 'minor' | 'moderate' | 'serious' | 'critical' | null | undefined
  description: string
  id: string
}

async function report() {
  // const url = 'https://denkwerk.com'
  const url = 'https://www.zalando.de/lauren-ralph-lauren-judy-t-shirt-basic-black-l4221d09m-q11.html'

  const browser = await puppeteer.launch({
    headless: 'new',
  })

  // Create a page
  const page = await browser.newPage()

  // Go to your site
  await page.goto(url)

  const list = await page.evaluate(() =>
    Array.from(
      document.querySelectorAll('meta'), (e: HTMLMetaElement) => ([e.name, e.content]),
    ).filter(l => ['og:title', 'og:description', 'description', 'twitter:title', 'twitter:description', 'author'].includes(l[0].toLowerCase())),
  )

  const title = await page.evaluate(() => document.title)

  const context = Object.fromEntries(list)
  context.title = title
  context.url = url
  console.log('context', context)

  const axeBuilder = await loadPage(
    browser,
    url,
  )
  const results: AxeResults = await axeBuilder.analyze()

  // console.log('violations', results.violations)

  const violations = results.violations
  const filteredResults: FilteredResult[] = violations.map(violation => ({
    id: violation.id,
    description: violation.description,
    help: violation.help,
    impact: violation.impact,
  }))

  console.log('results', filteredResults)

  await browser.close()

  return {
    report: filteredResults,
    context,
  }
}

report().then(async (results) => {
  console.log('a11y report:', results)
  console.log('Save result..')
  await saveStringToFile(results)
  console.log('Saved report to file...')
}).catch((e) => {
  console.log('catch', e)
})

// Define the string you want to save to a file
const content = 'Hello, this is a string to be saved to a file using ESM syntax.'

// Function to write the string to a file
async function saveStringToFile(data: any) {
  try {
    // Specify the file path
    const filePath = 'out/report.json'

    await writeFile(filePath, JSON.stringify(data), 'utf8', () => {
      console.log('callback')
    })

    console.log('String successfully saved to file:', filePath)
  }
  catch (error) {
    console.error('Error saving the string to file:', error)
  }
}
