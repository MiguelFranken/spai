import { BadRequestException, Controller, Get, Query } from '@nestjs/common'
import { A11yReportService } from '../services/a11y-report.service'

function isValidUrl(input: string): boolean {
  try {
    // eslint-disable-next-line no-new
    new URL(input)
    return true
  }
  catch (_) {
    return false
  }
}

@Controller()
export class A11yReportController {
  constructor(private readonly a11yReportService: A11yReportService) {}

  @Get()
  test() {
    return "hello world"
  }

  @Get('a11y-report')
  async getReport(@Query('url') url: string) {
    // Check if url is provided
    if (!url)
      throw new BadRequestException('URL parameter is required.')

    if (!isValidUrl(url))
      throw new BadRequestException('Invalid URL provided.')

    return await this.a11yReportService.generateReport(url)
  }
}
