FROM node:18-alpine
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm install
COPY . .
RUN npm run build
CMD ["npx", "vite", "preview", "--host", "0.0.0.0", "--port", "5173"]