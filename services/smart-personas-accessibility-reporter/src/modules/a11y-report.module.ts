import { Module } from '@nestjs/common'
import { A11yReportService } from '../services/a11y-report.service'
import { A11yReportController } from '../controllers/a11y-report.controller'

@Module({
  controllers: [A11yReportController],
  providers: [A11yReportService],
})
export class A11yReportModule {}
