# Face Detection For Python Demo
=====================================

This project demonstrates the use of the [Face Detection For Python using ONNX](https://github.com/IntelliProve/face-detection-onnx) package. Additionally, it showcases DevOps principles by incorporating testing with Pytest, linting with Black, and a CI/CD pipeline to build a Docker container using Kaniko and Apptainer.

## Table of Contents
-----------------

1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Testing](#testing)
5. [Linting](#linting)
6. [CI/CD Pipeline](#cicd-pipeline)
7. [Docker Container](#docker-container)
8. [Apptainer Container](#apptainer-container)
9. [Image Dataset](#image-dataset)

## Project Overview
-----------------

This project uses the [Face Detection For Python using ONNX](https://github.com/IntelliProve/face-detection-onnx) package which is an ONNX version of [Face Detection For Python](https://github.com/patlevin/face-detection-tflite). Those packages perform face recognition tasks. Using the ONNX version helps keeping the dependencies small and fast to install. The project structure is as follows:

* `face.py`: The main code including the test.
    * `face-gpu.py`: GPU version of the main code
* `.gitlab-ci.yml`: The GitLab CI/CD pipeline configuration file.
* `Dockerfile`: The Dockerfile used to build the Docker container.
* `face.def`: Apptainer definition file for the `face.py` application
    * `face-gpu.def`: Apptainer definition file for the `face-gpu.py` application
* `face.sh`: Bash script to perform face detection
    * `face.slurm`: Slurm script for submission on the ECMWF's cluster
    * `face-gpu.slurm`: Slurm script for submission on the ECMWF's cluster

## Requirements
------------

* Python 3.10+
* PyTorch 2.2+
* Facenet-pytorch 2.6.0
* Pytest 8+
* Black 25,1
* Kaniko
* Apptainer
* [Unconstrained Face Detection Dataset (UFDD)](https://ufdd.info/) (more details [below](#image-dataset))

## Installation
------------

To install the required python dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Testing
-------

To run the Pytest test cases, navigate to the project directory and run the following command:

```bash
pytest
```

## Linting
-------

To run the Black linter, navigate to the project directory and run the following command:

```bash
black .
```

## CI/CD Pipeline
----------------

The CI/CD pipeline is configured using GitHub Actions. The pipeline consists of the following stages:

1. Test: Runs the Pytest test cases.
2. Lint: Runs Black.
3. Build Docker Container: Builds the Docker container using Kaniko.
4. Build Apptainer Container Image: Builds the Apptainer image.

The pipeline configuration files are located in the `.gitlab_ci.yaml` file.

## Docker Container
-----------------

The Docker container is built using Kaniko. The Dockerfile is located in the project root directory.

To build the Docker container manually, navigate to the project directory and run the following command:

```bash
kaniko build --context . --destination facenet_docker.img
```

## Apptainer Container
----------------------

The container image file (`face.sif`) is built using [Apptainer](https://apptainer.org/docs/user/latest/) and a definition file (`face.def`) located in the project root directory.

To build the container image file manually, navigate to the project directory and run the following command:

```bash
apptainer build face.sif face.def
```

> [!NOTE]
> The same applies for the GPU definition file (`face-gpu.def`)

## Image Dataset
----------------

The images come from the [Unconstrained Face Detection Dataset (UFDD)](https://ufdd.info/), which need to be downloaded in form of a zip file (`UFDD_val.zip`) and extracted in the root directory.
