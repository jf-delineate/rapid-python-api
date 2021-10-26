[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img alt="delineate.io" src="https://github.com/delineateio/.github/blob/master/assets/logo.png?raw=true" height="75" />
  <h2 align="center">delineate.io</h2>
  <p align="center">portray or describe (something) precisely.</p>

  <h3 align="center">Fast API Example</h3>

  <p align="center">
    Demonstrate a potential combination of technologies to rapidly build and deploy Python APIs
    <br />
    <a href="https://github.com/delineateio/fast-api-example"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/delineateio/fast-api-example/issues">Report Bug</a>
    ·
    <a href="https://github.com/delineateio/fast-api-example/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The purpose of this repo is to demonstrate a potential combination of technologies to rapidly build and deploy APIs.

### Built With

* [FastAPI](https://fastapi.tiangolo.com/) is an API framework which is  high performance, easy to learn, fast to code, ready for production
* [Behave](https://github.com/behave/behave/tree/121e61c5598b7967fd8a2eb1833235b282dc3ca6) is a BDD Python framework for collaboration between developers, QA and non-technical or business team members
* [Build Packs](https://buildpacks.io/) is a [cncf](https://www.cncf.io/) project to transform application code into images to run on any cloud
* [Hashicorp Waypoint](https://www.waypointproject.io/) provides a modern workflow to build, deploy, and release across platforms.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

There are a number of local dependencies that are required.  If you are using `macOS` then you can use `brew` to install these.

```shell
brew install docker --cask
brew install httpie pack pyenv
brew install hashicorp/tap/waypoint
```

### Installation

```shell
# clone the repo
git clone https://github.com/delineateio/fast-api-example.git

# creates the virtual env
pyenv virtualenv 3.9.1 fast-api-example

# installs the tooling requirements
pip install -r requirements.txt

# installs the git hook for pre-commit
pre-commit install
```

<!-- USAGE EXAMPLES -->
## Usage

### Run Native

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
# run the commands in ./src
cd ./.src

# start the waypoint server locally
waypoint install --platform=docker -accept-tos

# generate the waypoint token
waypoint user token new

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

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/delineateio/fast-api-example/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

If you would like to contribute to any Capco Digital OSS projects please read:

* [Code of Conduct](https://github.com/delineateio/.github/blob/master/CODE_OF_CONDUCT.md)
* [Contributing Guidelines](https://github.com/delineateio/.github/blob/master/CONTRIBUTING.md)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Best README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/delineateio/fast-api-example.svg?style=for-the-badge
[contributors-url]: https://github.com/delineateio/fast-api-example/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/delineateio/fast-api-example.svg?style=for-the-badge
[forks-url]: https://github.com/delineateio/fast-api-example/network/members
[stars-shield]: https://img.shields.io/github/stars/delineateio/fast-api-example.svg?style=for-the-badge
[stars-url]: https://github.com/delineateio/fast-api-example/stargazers
[issues-shield]: https://img.shields.io/github/issues/delineateio/fast-api-example.svg?style=for-the-badge
[issues-url]: https://github.com/delineateio/fast-api-example/issues
[license-shield]: https://img.shields.io/github/license/delineateio/fast-api-example.svg?style=for-the-badge
[license-url]: https://github.com/delineateio/fast-api-example/blob/master/LICENSE
