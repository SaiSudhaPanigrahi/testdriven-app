# base image
FROM node:12.13.1-alpine

# install global packages
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
RUN npm install npm@latest -g
RUN npm install pnpm react-scripts@3.3.0 -g

# set working directory
WORKDIR /usr/src/app

# install dependencies
COPY package*.json /usr/src/app/
COPY pnpm-lock.yaml /usr/src/app/pnpm-lock.yaml
ENV PATH /usr/src/app/node_modules/.bin:$PATH
ENV PATH=$PATH:/home/node/.npm-global/bin
RUN pnpm install

# start app
CMD ["npm", "start"]
