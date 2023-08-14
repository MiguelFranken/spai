import { Injectable } from '@nestjs/common';
import {injectAxe, getAxeResults} from "axe-playwright";

const { chromium, webkit } = require('playwright');

interface FilteredResult {
    help: string
    impact: 'minor' | 'moderate' | 'serious' | 'critical' | null | undefined
    description: string
    id: string
}

export type AccessibilityReport = { report: FilteredResult[], context: any }

@Injectable()
export class A11yReportService {
    async generateReport(): Promise<AccessibilityReport> {
        const url = 'https://denkwerk.com'

        let browser;

        try {
            browser = await chromium.launch({
                args: ['--no-sandbox']
            });
        } catch(e) {
            browser = await webkit.launch();
        }

        const contextBrowser = await browser.newContext();
        const page = await contextBrowser.newPage();

        await page.goto(url);

        await injectAxe(page)

        const list = await page.evaluate(() =>
            Array.from(
                document.querySelectorAll('meta'), (e: HTMLMetaElement) => ([e.name, e.content]),
            ).filter(l => ['og:title', 'og:description', 'description', 'twitter:title', 'twitter:description', 'author'].includes(l[0].toLowerCase())),
        )

        const title = await page.evaluate(() => document.title)

        const context = Object.fromEntries(list)
        context.title = title
        context.url = url


        const results = await getAxeResults(page)

        const violations = results.violations
        const filteredResults: FilteredResult[] = violations.map(violation => ({
            id: violation.id,
            description: violation.description,
            help: violation.help,
            impact: violation.impact,
        }))

        await browser.close()

        return {
            report: filteredResults,
            context,
        }
    }
}