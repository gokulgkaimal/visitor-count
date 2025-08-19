Visitor Count App (Python)

A lightweight Python Flask application that displays and tracks the number of visitors. This project demonstrates Dockerization and CI/CD integration using GitHub Actions.

##  Features

- Visitor count displayed on a web page
- Built using Python and Flask
- Dockerized for easy deployment
- CI pipeline with GitHub Actions
- Docker image pushed to Docker Hub automatically

##  Tech Stack

- **Backend**: Python 3, Flask
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Registry**: Docker Hub

##  How to Run

### 1. Clone the Repository


git clone https://github.com/your-username/visitor-count-app.git
cd visitor-count-app
2. Run with Docker

docker build -t visitor-count-app .
docker run -p 5000:5000 visitor-count-app
Visit http://localhost:5000 in your browser.

 CI with GitHub Actions
.github/workflows/docker.yml handles:

Building the Docker image

Logging into Docker Hub

Pushing the image to your Docker repository

 Ensure you add the following secrets in your GitHub repo:

DOCKER_USERNAME

DOCKER_PASSWORD
