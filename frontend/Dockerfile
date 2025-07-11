# Stage 1: Build the Angular frontend
FROM node:20-alpine as build

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build -- --configuration=production

# Stage 2: Serve with NGINX
FROM nginx:1.28-alpine

# Copy built files from Angular output
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html

EXPOSE 80
