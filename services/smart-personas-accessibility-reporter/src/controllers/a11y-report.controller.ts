import { Controller, Get, Query, BadRequestException } from '@nestjs/common';
import { A11yReportService } from '../services/a11y-report.service';

@Controller('a11y-report')
export class A11yReportController {
    constructor(private readonly a11yReportService: A11yReportService) {}

    @Get()
    async getReport(@Query('url') url: string) {
        // Check if url is provided
        if (!url) {
            throw new BadRequestException("URL parameter is required.");
        }

        // Validate URL
        try {
            new URL(url);
        } catch (_) {
            throw new BadRequestException("Invalid URL provided.");
        }

        return await this.a11yReportService.generateReport(url)
    }
}