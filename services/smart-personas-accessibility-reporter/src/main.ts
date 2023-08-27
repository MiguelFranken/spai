import { NestFactory } from '@nestjs/core'
import { AppModule } from './app.module'

async function bootstrap() {
  const app = await NestFactory.create(AppModule)
  app.enableCors()

  // eslint-disable-next-line n/prefer-global/process
  const port = process.env.PORT ? Number.parseInt(process.env.PORT) : 3000

  await app.listen(port)
}
bootstrap()
