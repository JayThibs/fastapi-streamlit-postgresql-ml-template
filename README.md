# Project Template for Creating an ML App with FastAPI, Streamlit and PostgreSQL

This repo is meant as a template for projects using FastAPI and Streamlit for ML projects. A model is trained with the Bank Notes dataset in order to predict whether a Bank Note is fake or not.

You can create the environment to test out the project by simply running the following commands in the root directory:

1. `make conda-update` to add exact Python and CUDA versions.
2. `conda activate fastapi-streamlit-ml` to create conda environment.
3. `make poetry` to install all Python dependencies.
4. Create a .env file in the root directory with the following environment variables:

        DB_USER
        DB_PASSWORD
        DB_HOST
        DB_PORT
        DB_NAME

5. `make run-db` to create our PostgreSQL database with Docker
