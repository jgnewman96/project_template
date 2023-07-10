# pull official base image
FROM node:20-alpine3.17

# set working directory
WORKDIR /src/frontend
ENV PATH src/frontend/node_modules/.bin:$PATH


# install app dependencies
COPY package.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

# add app
COPY . ./