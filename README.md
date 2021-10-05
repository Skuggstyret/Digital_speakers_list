## Goal

Simplify meeting by providing a digital speakers list. In with member can sign up and raise and lower their hands. Additionally simplify meetings by automatically handling the speaking list included next speaker, cleaning the list, and nested lists.

## License

MIT, see LICENSE.md

## Installation

Download the repo by pressing _code_ and _Download ZIP_, or by

```
git clone https://github.com/Skuggstyret/Digital\_talarlista
```

## Usage

Start production server by

```
docker-compose -f deployment.yml up
```

Requires docker and docker-compose.

The `-d` flag to run the system in the background, to terminate the system use

```
docker-compose -f deployment.yml down
```

Probably windows on windows docker too but don't ask my how windows docker works, because I have no idea.

## Contribute

Same as above but change the yml file to `development.yml`, this will start the backend in development providing more feedback. To run the frontend for development enter the `frontend` and run.

```
yarn install
```

to install dependencies

```
yarn serve
```

to start the frontend.

Both the frontend and backend in development mode will hot load changes, with the exception of change to the backend config file.

Requires yarn.

If you want to contribute a change then please a pull request to main and we'll look at it at out earliest convinces.

## Possible improvements

- Rewrite in better language, _cough_ Rust _cough_.
- Improved usability.
- Add support for locking down certain or all feature to prevent tampering.
- Setup CI, to provide docker images through ghcr.
- Provide support for an arbitrary number meetings and create/destroy meeting
