# Use the official Node.js image as a parent image
FROM node:18-alpine AS build

# Set the working directory in the container
WORKDIR /usr/src/app

RUN npm install -g pnpm

# packages change infrequently compared to source code
COPY package.json pnpm-lock.yaml* ./
RUN pnpm install

# Copy the rest of the application code
COPY . .

# Build the NestJS application for production
RUN pnpm run build

# Use Playwright's official Docker base image
FROM mcr.microsoft.com/playwright:v1.37.0-jammy

WORKDIR /usr/src/app

# Install pnpm
RUN npm install -g pnpm

# Install only production dependencies using pnpm
COPY --from=build /usr/src/app/pnpm-lock.yaml* ./
COPY --from=build /usr/src/app/package.json ./
RUN pnpm install --prod

# Copy the built app from the previous step
COPY --from=build /usr/src/app/dist ./dist

# Define the command to run the application
CMD ["pnpm", "start:prod"]