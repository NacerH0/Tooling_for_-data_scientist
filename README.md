<div align="center">

# Project Overview

This project provides an app that takes Excel files as input and return graphs as outputs. It includes Docker support to easily run the application in a containerized environment.

## Table of Contents

- []

  - [Installation]
  - [Usage](#usage)
  - [Repository Structure](#repository-structure)


## Prerequesites
Before you begin, ensure you have the following installed on your machine:
- Docker 
- Python 
- pip 
- virtualenv 

## Installation

To set up the project locally:

- Clone the repository to your local machine:

git clone https://github.com/your-username/Tooling_for_-data_scientist.git
cd Tooling_for_-data_scientist

- Set up a virtual environment to manage the project dependencies:

python3 -m venv venv

- Activate the Virtual Environment :

On macOS/Linux:
source venv/bin/activate
On Windows:
.\venv\Scripts\activate


```

## Usage

Running the App Locally :

- Use Streamlit to run the app locally after you installed the requirements:
streamlit run app.py

- The app will open in your browser at http://localhost:8501. You can upload an Excel file and view the generated graphs.

Running the App with Docker :

- To build the Docker image, run the following command in the root of the repository:
docker build -t data-scientist-tooling .

- Once the image is built, you can run the application inside a Docker container:
docker run -p 8501:8501 data-scientist-tooling
This command will run the app on port 8501. You can access the application by navigating to http://localhost:8501.

To stop the running container, use:
docker ps
docker stop <container_id>


## Repository Structure

```
.
├── Dockerfile: Defines the Docker image configuration.
├── app.py: The main Python application.
├── requirements.txt: Lists the Python dependencies for the project.
├── .gitignore: Specifies files and directories to ignore in Git.
├── README.md: Project documentation (this file).
```
