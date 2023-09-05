FROM node:lts

RUN mkdir /front
WORKDIR /front
ADD . /front

RUN apt update && apt install bash
# RUN npm config set fetch-retry-mintimeout 20000
# RUN npm config set fetch-retry-maxtimeout 120000
RUN npm install -g npm@9.8.1
RUN npm install
RUN npm run build

EXPOSE 5173

CMD ["npm", "run", "dev"]
# CMD ["npm", "run", "build"]