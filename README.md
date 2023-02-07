# About The CI Challenge

In this challenge, I set up a repository and CI pipeline on GitHub that, upon a repository code change, builds and tests a set of microservices, then deploys docker images to an DockerHub repository.

## Built With

* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
* ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Prerequisites

Basic knowledge of Flask, Python, Docker, and CURL. 
Write:

* Python script that sends an HTTP request to microservices
* Dockerfile for Flask app
* workflow for CI to set up the parallel jobs and define each job as a separate step in a YAML file.

### About the challenge

- [x] Create 3 microservices (Flask): microservice_a, microservice_b, and microservice_c.
- [x] Create a script (Python) that tests each microservice by sending it an HTTP request.
- [x] When the test script sends an HTTP request to microservice_a or microservice_b, it should succeed with a 200 response code.
- [x] When the test script sends an HTTP request to microservice_c, it should fail with a 500 response code.
- [ ] Each microservice should have a script (bash, etc.) that builds its docker image. 
- [x] The pipeline should build these docker images in parallel. 
If any docker image fails to build successfully, then the pipeline should fail.
- [x] Once the docker images are built, use the test script to send HTTP requests to each microservice. This should result in microservice_a and microservice_b passing, but microservice_c failing.
- [x] Deploy the passing docker images to the image repository.
Conclude the CI pipeline with the appropriate status.

### Build the docker image

To build the docker image, the GitHub module was taken instead of the script, thereby reducing the human factor and improving the readability of the code.