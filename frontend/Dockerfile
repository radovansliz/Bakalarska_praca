FROM node:lts-alpine

RUN apk add curl
RUN curl -f https://get.pnpm.io/v6.16.js | node - add --global pnpm

RUN mkdir /frontend
WORKDIR /frontend
COPY package*.json ./

COPY . .

RUN pnpm install

EXPOSE 3000

CMD ["pnpm", "run", "dev", "--host", "0.0.0.0", "--port", "3000"]