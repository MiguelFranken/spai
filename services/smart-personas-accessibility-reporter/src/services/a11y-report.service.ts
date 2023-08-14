import { Injectable } from '@nestjs/common'
import { getAxeResults, injectAxe } from 'axe-playwright'

import type { Browser, BrowserContext, Page } from 'playwright'

import { chromium, webkit } from 'playwright' // Use typed imports instead of require

interface FilteredResult {
  help: string
  impact: 'minor' | 'moderate' | 'serious' | 'critical' | null | undefined
  description: string
  id: string
}

export interface AccessibilityReport { report: FilteredResult[]; context: any }

@Injectable()
export class A11yReportService {
  /**
     * Generates an accessibility report for the given URL.
     * @param url - The URL to generate the report for.
     * @returns A Promise that resolves to an AccessibilityReport object containing the filtered results and context.
     */
  async generateReport(url: string): Promise<AccessibilityReport> {
    const browser = await this.launchBrowser()
    const page = await this.openPage(browser, url)

    await injectAxe(page)

    const context = await this.extractContext(page, url)
    const filteredResults = await this.extractResults(page)

    await browser.close()

    return {
      report: filteredResults,
      context,
    }
  }

  /**
     * Launches a browser instance using either Chromium or WebKit.
     * @returns A Promise that resolves to a Browser instance.
     */
  private async launchBrowser(): Promise<Browser> {
    try {
      return await chromium.launch({
        args: ['--no-sandbox'],
      })
    }
    catch (e) {
      return await webkit.launch()
    }
  }

  /**
     * Opens a new page in a browser context and navigates to the specified URL.
     * @param browser The browser instance to use.
     * @param url The URL to navigate to.
     * @returns A Promise that resolves to the newly created Page object.
     */
  private async openPage(browser: Browser, url: string): Promise<Page> {
    const contextBrowser: BrowserContext = await browser.newContext()
    const page: Page = await contextBrowser.newPage()
    await page.goto(url)
    return page
  }

  /**
     * Extracts relevant context information from the given page and URL.
     * @param {Page} page - The page to extract context from.
     * @param {string} url - The URL of the page.
     * @returns {Promise<any>} - A promise that resolves to an object containing the extracted context information.
     */
  private async extractContext(page: Page, url: string): Promise<any> {
    const list = await page.evaluate(() =>
      Array.from(
        document.querySelectorAll('meta'),
        (e: HTMLMetaElement) => ([e.name, e.content]),
      ).filter(l => ['og:title', 'og:description', 'description', 'twitter:title', 'twitter:description', 'author'].includes(l[0].toLowerCase())),
    )

    const title = await page.evaluate(() => document.title)
    const context = Object.fromEntries(list)
    context.title = title
    context.url = url

    return context
  }

  /**
     * Extracts filtered accessibility results from a given Puppeteer page using Axe.
     * @param page - The Puppeteer page to extract results from.
     * @returns An array of filtered accessibility results.
     */
  private async extractResults(page: Page): Promise<FilteredResult[]> {
    const results = await getAxeResults(page)

    return results.violations.map(violation => ({
      id: violation.id,
      description: violation.description,
      help: violation.help,
      impact: violation.impact,
    }))
  }
}
