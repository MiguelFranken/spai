import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import {A11yReportModule} from "./modules/a11y-report.module";

@Module({
  imports: [A11yReportModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
