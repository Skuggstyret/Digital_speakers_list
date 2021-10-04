# charm_ticket

The frontend is built in [Vue 2.9](https://vuejs.org/). It also uses the [Vuetify](https://vuetifyjs.com/en/) and [Vuex](https://vuex.vuejs.org/) vue plugins.

## Project setup

### Development
Run the `docker-compose.yml -d` in the parent directory to start the docker-container

In order to get feedback from the dev-server on code errors in CLi remove the `-d` flag (you get output from all containers). Attach to the container if you only want that specific containers output.

On windows just check the logs in the GUI.

The project is set up with ESLint + prettier, the wdev server will complain and fail on compilation if the linting isn't up to par. So make sure you have a ESLint pluggin installed to show the errors in your editor.

#### Adding dependencies
To add dependencies make sure you have yarn installed. (not NPM, might give package version errors)

With yarn installed run `yarn add [package]` and then rebuild the docker container with `docker-compose up --build`

In order to add vue plugins you need to add `@vue/cli` as a global dependency in yarn with `yarn global add @vue/cli`
