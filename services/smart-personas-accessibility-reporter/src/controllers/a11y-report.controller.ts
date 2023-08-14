import { Controller, Get } from '@nestjs/common';
import { A11yReportService } from '../services/a11y-report.service';

@Controller('a11y-report')
export class A11yReportController {
    constructor(private readonly a11yReportService: A11yReportService) {}

    @Get()
    async getReport() {
        return await this.a11yReportService.generateReport()
    }
}