import os
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET", "local-weather-bucket")
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE", "WeatherLogs")
CACHE_EXPIRY = int(os.getenv("CACHE_EXPIRY", 300))  # Cache expiry in seconds (5 minutes)

# Check if AWS credentials are provided
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

USE_AWS = AWS_ACCESS_KEY_ID is not (None or "")

# Local storage paths
LOCAL_STORAGE_PATH = os.path.join(BASE_DIR, "tmp", "weather_data")
LOCAL_LOG_FILE = os.path.join(BASE_DIR, "tmp", "weather_logs.json")

# Ensure local storage directories exist
os.makedirs(LOCAL_STORAGE_PATH, exist_ok=True)


WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", None)
