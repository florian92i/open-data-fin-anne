FROM node:13

WORKDIR /app

COPY package.json .

RUN npm install --quiet

COPY . .

EXPOSE 3000

CMD npm dev
