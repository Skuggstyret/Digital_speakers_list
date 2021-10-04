# FROM node
#
# WORKDIR /app
#
# # Install packages using Yarn
# ADD package.json yarn.lock /tmp/
# RUN cd /tmp && yarn
# RUN mkdir -p /app && cd /app && ln -s /tmp/node_modules && ln -s /tmp/package.json
#
# CMD yarn run serve --host 0.0.0.0


FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]
