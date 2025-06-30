# Face Detection For Python Demo

This project demonstrates the use of the [Face Detection For Python using ONNX](https://github.com/IntelliProve/face-detection-onnx) package. Additionally, it showcases DevOps principles by incorporating testing with Pytest, linting with Black, and a CI/CD pipeline to build a Docker container using Kaniko and Singularity.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Testing](#testing)
5. [Linting](#linting)
6. [CI/CD Pipeline](#cicd-pipeline)
7. [Docker Container](#docker-container)
8. [Singularity Container](#singularity-container)

## Project Overview

This project uses the [Face Detection For Python using ONNX](https://github.com/IntelliProve/face-detection-onnx) package which is an ONNX version of [Face Detection For Python](https://github.com/patlevin/face-detection-tflite). Those packages perform face recognition tasks. Using the ONNX version helps keeping the dependencies small and fast to install. The project structure is as follows:

* `face.py`: The main code including the test.
* `.gitlab-ci.yml`: The GitLab CI/CD pipeline configuration file.
* `Dockerfile`: The Dockerfile used to build the Docker container.
* `Singularity.def`: The Singularity definition file used to build the Singularity container.

## Requirements

* Python 3.10+
* PyTorch 2.2+
* Facenet-pytorch 2.6.0
* Pytest 8+
* Black 25,1
* Kaniko
* Singularity

## Installation

To install the required python dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Testing

To run the Pytest test cases, navigate to the project directory and run the following command:

```bash
pytest
```

## Linting

To run the Black linter, navigate to the project directory and run the following command:

```bash
black .
```

## CI/CD Pipeline

The CI/CD pipeline is configured using GitHub Actions. The pipeline consists of the following stages:

1. Test: Runs the Pytest test cases.
2. Lint: Runs Black.
3. Build Docker Container: Builds the Docker container using Kaniko.
4. Build Singularity Container Image : Builds the Singularity container.

The pipeline configuration files are located in the `.gitlab_ci.yaml` file.

## Docker Container

The Docker container is built using Kaniko. The Dockerfile is located in the project root directory.

To build the Docker container manually, navigate to the project directory and run the following command:

```bash
kaniko build --context . --destination facenet_docker.img
```

## Singularity Container

The Singularity container is built using Singularity. The Singularity definition file is located in the project root directory.

To build the Singularity container manually, navigate to the project directory and run the following command:

```bash
singularity build facenet_docker.img Singularity.def
```

