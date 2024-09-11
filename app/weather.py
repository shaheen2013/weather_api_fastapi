import aiohttp
from fastapi import HTTPException
from app.config import WEATHER_API_KEY


WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

async def fetch_weather(city: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(WEATHER_API_URL, params={"q": city, "appid": WEATHER_API_KEY}) as response:
                if response.status != 200:
                    raise HTTPException(status_code=response.status, detail=f"Error fetching weather data: {await response.text()}")
                return await response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
