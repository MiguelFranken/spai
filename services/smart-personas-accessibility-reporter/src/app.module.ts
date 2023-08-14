import { Module } from '@nestjs/common';
import {A11yReportModule} from "./modules/a11y-report.module";

@Module({
  imports: [A11yReportModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
