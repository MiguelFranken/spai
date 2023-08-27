FROM node:18-alpine AS base

WORKDIR /app

# Set node_modules path so global installs aren't required
ENV PATH /app/node_modules/.bin:$PATH

# Install pnpm
RUN npm install --global pnpm

FROM base AS dependencies

COPY package*.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./
COPY ./app/package*.json ./app/

# Install the application dependencies
RUN pnpm install --no-frozen-lockfile

FROM dependencies AS build

# Copy all files
COPY . .

# Build the application
RUN pnpm --filter @denkwerk/smart-personas-frontend build 

FROM node:18-alpine AS release

WORKDIR /app

# Copy only necessary files for runtime
COPY --from=build /app/app/.output ./.output

# Set the entry point
CMD ["node", ".output/server/index.mjs"]