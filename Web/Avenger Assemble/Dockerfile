FROM node:18-slim

WORKDIR /usr/src/app

COPY ./src/package.json ./

RUN npm install --only=production

COPY ./src .

EXPOSE 8386

CMD ["node", "index.js"]
