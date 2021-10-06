## Goal

Simplify meeting by providing a digital speakers list. That allows meeting participants can sign up in order to raise and lower their hands remotely. As well as simplifying the meetings by automatically handling the speaking list to give the next speaker, clearing the list, and handling nestling the lists

## License

MIT, see LICENSE.md

## Installation

Download the repo by pressing _code_ and _Download ZIP_, or by

```
git clone https://github.com/Skuggstyret/Digital\_talarlista
```

## Usage

Start production server (frontend & backend) by

```
docker-compose -f deployment.yml up
```

Requires docker and docker-compose.
The `-d` flag can be used to run the system in the background.

To terminate the system use
```
docker-compose -f deployment.yml down
```

Note: In order to make the frontend work in production you need to make your webserver handle Vue Routers History mode. For information on how visit [this page](https://router.vuejs.org/guide/essentials/history-mode.html#example-server-configurations)


Probably windows on windows docker too but don't ask me how windows docker works, because I have no idea.

## Development

Same as above but change the yml file to `development.yml`, 
```
docker-compose -f development.yml down
```
This starts the backend in development which provides more feedback. 

To run the frontend for development enter the `frontend` directory and run.
install dependencies with
```
yarn install
```

to start the frontend in webpacks dev server
```
yarn serve
```

Both the frontend and backend in development mode will hot load changes, with the exception of changes to the backend config file or installation of new dependencies to python or node

If you want to contribute a change then please a pull request to main and we'll look at it at when we have time.

## Possible improvements


- Add support for authentication in order to lock down certain or all feature to prevent tampering
- Rewrite backend in better language, such as Rust, mostly for fun.
- Improved usability.
- Setup CI, to provide docker images through ghcr.
- Provide support for an arbitrary number meetings and creation/destroy meeting
- create configuration to change and modify features such as nesting and ordering of speakers
- Create a database for the backend to use, to save states between restarts
