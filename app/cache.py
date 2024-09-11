import os
import time
import json

from app.config import CACHE_EXPIRY

CACHE_DIR = "/tmp/weather_cache"

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def get_cached_weather(city: str):
    cache_path = os.path.join(CACHE_DIR, f"{city}.json")
    if os.path.exists(cache_path):
        file_time = os.path.getmtime(cache_path)
        if time.time() - file_time < CACHE_EXPIRY:
            with open(cache_path, "r") as f:
                return json.load(f)
    return None

def set_cached_weather(city: str, data: dict):
    cache_path = os.path.join(CACHE_DIR, f"{city}.json")
    with open(cache_path, "w") as f:
        json.dump(data, f)
