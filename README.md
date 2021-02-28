<p align="center">
  <img alt="delineate.io" src="https://github.com/delineateio/.github/blob/master/assets/logo.png?raw=true" height="75" />
  <h2 align="center">delineate.io</h2>
  <p align="center">portray or describe (something) precisely.</p>
</p>

# Demo Rapid Python API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg)](https://github.com/delineateio/box/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22+)

## Purpose

The purpose of this repo is to demonstrate a potential combination of technologies to rapidly build and deploy APIs.

Specifically this demonstrates the following combination of technologies:

* [FastAPI](https://fastapi.tiangolo.com/) is an API framework which is  high performance, easy to learn, fast to code, ready for production
* [Behave](https://github.com/behave/behave/tree/121e61c5598b7967fd8a2eb1833235b282dc3ca6) is a BDD Python framework for collaboration between developers, QA and non-technical or business team members
* [Build Packs](https://buildpacks.io/) is a [cncf](https://www.cncf.io/) project to transform application code into images to run on any cloud
* [Hashicorp Waypoint](https://www.waypointproject.io/) provides a modern workflow to build, deploy, and release across platforms.

## Contributing

Contributions to this project are welcome!

* [Contribution Guidelines](https://github.com/delineateio/.github/blob/master/CONTRIBUTING.md)
* [Code of Conduct](https://github.com/delineateio/.github/blob/master/CODE_OF_CONDUCT.md)

Please note that [git commit signing](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work) is required to contribute to this project.

## Running Locally

### Native

```shell
# runs the server
uvicorn main:app --reload --app-dir src

# runs the tests
behave tests

# health check
http :8000/healthz

# companies
http :8000/company/03638404 # Capco
http :8000/company/00048839 # Barclays
```

### Build Packs

```shell
# builds the image based on heroku buildpacks
pack build companies-api --path ./src --builder heroku/buildpacks:18

# runs the container on the standard port
docker run -d -p 8000:8000 --name companies-api companies-api

# cleans up
docker rm companies-api -f && docker system prune -f
```

### Waypoint

```shell
# start the waypoint server locally
waypoint install --platform=docker -accept-tos

# generate the waypoint token
waypoint token new

# initialises the directory
waypoint init

# deploys the app
waypoint up

# destroys the app
waypoint destroy
```

### Docker Commands

```shell
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}'
```
