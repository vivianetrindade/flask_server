<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/vivianetrindade/flask_server">
    <!-- <img src="client/public/images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

  <h3 align="center">Flask Server</h3>
  <p align="center">
      The project is a simple flask server app.
      <br />
      <a href="https://github.com/vivianetrindade/flask_server"><strong>Explore the docs »</strong></a>
      <br />
      <br />
      <!-- <a href="https://github.com/github_username/repo_name">View Demo</a> -->
      ·
      <a href="https://github.com/vivianetrindade/flask_server/issues">Report Bug</a>
      ·
      <a href="https://github.com/vivianetrindade/flask_server/issues">Request Feature</a>
    </p>
</div>

<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

The main goal of this project is to create a simple flask server app where connected to SQLite database you can GET information about people in the queue for a place and POST new people in the database.
The project has a Dockerfile and a shell script to build and run the resulting Docker image. When the shell script is used, an interactive bash-shell is opened in the Docker image.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.py]][Python-url]
* [![Flask][Flask.py]][Flask-url]
* [![SQLite3][SQLite3.py]][SQLite3-url]
* [![Docker][Docker.py]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

This is instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You need to have installed:
- [Docker](https://docs.docker.com/get-docker/)
- Python 3.8.5

### Installation

1. Clone the repo
   ```sh
   git clone
    ```
2. Install Docker packages
    ```sh
    sh build_and_run.sh
    ```
The shell script will build the Docker image and run it. And you will be able to access the flask server app in your browser at http://localhost:5001  or using any platform to test APIs like Postman.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

The endpoints created are:
-  GET /users - returns the first and last names of all users in the database.
-  GET /queues - returns all the queues that exist and the cities they are in.
-  GET /admin/inactive - returns users that does not have any "active" positions in a queue.
-  GET /user/<name> - returns all the queues that the user is currently active in.
-  POST /user - given a new users first name, last name and age inserts this into the database.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [ ] Add endpoint for POST /queue
- [ ] Add endpoint for POST /user_to_queue
- [ ] Add endpoint for POST /city
- [ ] Add endpoint for POST /city_to_queue

See the [open issues](https://github.com/vivianetrindade/flask_server) for a list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Viviane Trindade - [@linkedin_handle](https://www.linkedin.com/in/viviane-trindade/) - trindade.vivine@gmail.com
Portfolio: [https://vivianetrindadeportfolio.onrender.com/](https://vivianetrindadeportfolio.onrender.com/)
Project Link: [https://github.com/vivianetrindade/flask_server](https://github.com/vivianetrindade/flask_server)

<p align="right">(<a href="#readme-top">back to top</a>)</p> 

## Acknowledgments

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/vivianetrindade/flask_server.svg?style=for-the-badge
[contributors-url]: https://github.com/vivianetrindade/flask_server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vivianetrindade/flask_server.svg?style=for-the-badge
[forks-url]: https://github.com/vivianetrindade/flask_server/network/members
[stars-shield]: https://img.shields.io/github/stars/vivianetrindade/flask_server.svg?style=for-the-badge
[stars-url]: https://github.com/vivianetrindade/flask_server/stargazers
[issues-shield]: https://img.shields.io/github/issues/vivianetrindade/flask_server.svg?style=for-the-badge
[issues-url]: https://github.com/vivianetrindade/flask_server/issues
[license-shield]: https://img.shields.io/github/license/vivianetrindade/flask_server.svg?style=for-the-badge
[license-url]: https://github.com/vivianetrindade/flask_server/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/viviane-trindade/
[Python.py]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Flask.py]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Docker.py]: https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white
[SQLite3.py]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[Python-url]: https://www.python.org/
[Flask-url]: https://flask.palletsprojects.com/en/2.0.x/
[Docker-url]: https://www.docker.com/
[SQLite3-url]: https://www.sqlite.org/index.html

