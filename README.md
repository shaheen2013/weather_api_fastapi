# Overview

A weather API service built with FastAPI, fetching data from external APIs like OpenWeatherMap, with optional AWS S3/DynamoDB or local storage.

# Setup & Run

### Clone and Navigate

git clone https://github.com/your-username/weather-api.git
cd weather-api


### Configure Environment

Create a .env file based on the sample_env

### Run Locally

- With Python:

`pip install -r requirements.txt`

`uvicorn app.main:app --reload`

- Or with Docker:

`docker-compose up --build`


# Notes

- Default local storage at /tmp/weather_data.
- Ensure AWS credentials in .env for AWS integration.