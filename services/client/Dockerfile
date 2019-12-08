# base image
FROM node:12.12.0-alpine

# set working directory
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package*.json /usr/src/app/
COPY pnpm-lock.yaml /usr/src/app/pnpm-lock.yaml
RUN npm install pnpm react-scripts@3.3.0 -g --silent
RUN chown -R node:node . && chmod -R 755 .
USER node
RUN pnpm install --silent

# start app
CMD ["npm", "start"]
