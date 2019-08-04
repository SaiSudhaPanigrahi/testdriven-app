<!-- PROJECT SHIELDS -->
<!--
-->

[![Build Status][build-shield]][build-url]
[![Contributors][contributors-shield]][contributors-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/sophiabrandt/testdriven-app">
    <img src="logo.png" alt="Logo">
  </a>

  <h3 align="center">TestDriven App</h3>

  <p align="center">
    Microservices with Docker, Flask, and React
    <br />
    <a href="https://github.com/sophiabrandt/testdriven-app"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/sophiabrandt/testdriven-app">View Demo</a>
    ·
    <a href="https://github.com/sophiabrandt/testdriven-app/issues">Report Bug</a>
    ·
    <a href="https://github.com/sophiabrandt/testdriven-app/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project

This repository mirrors my progress for the course **[Microservices with Docker, Flask and React][testdriven]**.

### Built With

- [Flask](https://palletsprojects.com/p/flask/)
- [Docker](https://www.docker.com/)
- [React](https://reactjs.org)
- [Bulma CSS](https://bulma.io/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This project uses **Docker** and **docker-compose**.  
Please make sure to install both on your system. See [Docker Documentation](https://docs.docker.com/) for details.

### Installation

1. Clone the repo:

```sh
git clone https://github.com/sophiabrandt/testdriven-app.git
```

2. Build the containers:

```sh
docker-compose build
```

3. Start the containers (in the background):

```sh
docker-compose up -d
```

4. Seed the database:

```sh
docker-compose exec users python manage.py seed_db
```

5. Run tests:

```sh
docker-compose exec users python manage.py test
```

<!-- USAGE EXAMPLES -->

## Usage

The React app is available at `http://localhost`.

The users endpoint is available at `http://localhost/users`.

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/sophiabrandt/testdriven-app/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Please note that this is a learning repo and not a real app.**

<!-- LICENSE -->

## License

Code is &copy; 2019 Michael Herman. Minor adjustments by Sophia Brandt.

<!-- CONTACT -->

## Contact

Sophia Brandt - [@hisophiabrandt](https://twitter.com/hisophiabrandt)

Project Link: [https://github.com/sophiabrandt/testdriven-app](https://github.com/sophiabrandt/testdriven-app)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Microservices with Docker, Flask, and React][testdriven]
- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Best-README-Template][bestreadmetemplate]
- [Travis CI](https://travis-ci.org/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[build-shield]: https://travis-ci.org/sophiabrandt/testdriven-app.svg?branch=master
[build-url]: https://travis-ci.org/sophiabrandt/testdriven-app
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[contributors-url]: https://github.com/sophiabrandt/testdriven-app/graphs/contributors
[bestreadmetemplate]: https://github.com/othneildrew/Best-README-Template
[testdriven]: https://testdriven.io/courses/microservices-with-docker-flask-and-react/
