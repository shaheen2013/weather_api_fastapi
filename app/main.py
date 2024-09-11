from fastapi import FastAPI, HTTPException, Query
from app.weather import fetch_weather
from app.s3_client import upload_to_storage
from app.dynamodb_client import log_event
from app.cache import get_cached_weather, set_cached_weather
from datetime import datetime


app = FastAPI()

@app.get("/weather")
async def get_weather(city: str = Query(..., description="City name to get weather data for")):
    # Check cache first
    cached_data = get_cached_weather(city)
    if cached_data:
        return cached_data

    # Fetch from external API
    weather_data = await fetch_weather(city)

    # Save to S3 or locally and log the event
    storage_url = await upload_to_storage(city, weather_data)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    await log_event(city, timestamp, storage_url)

    # Cache the result
    set_cached_weather(city, weather_data)

    return weather_data
