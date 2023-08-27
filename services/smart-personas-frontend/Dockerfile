FROM node:18-alpine AS build

WORKDIR /app

RUN npm install --global pnpm
COPY . .
RUN pnpm install --no-frozen-lockfile
RUN pnpm --filter @denkwerk/smart-personas-frontend build 


FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy only necessary files for runtime
COPY --from=build /app/app/.output ./.output

EXPOSE 3000

# Set the entry point
CMD ["node", ".output/server/index.mjs"]