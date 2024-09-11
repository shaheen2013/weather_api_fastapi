import asyncio
import os
import json
from datetime import datetime
from aiobotocore.session import get_session
from app.config import DYNAMODB_TABLE, USE_AWS, LOCAL_LOG_FILE

async def log_event(city: str, timestamp: str, storage_url: str):
    log_entry = {
        'city': city,
        'timestamp': timestamp,
        'storage_url': storage_url
    }

    if USE_AWS:
        # Use AWS DynamoDB
        session = get_session()
        async with session.create_client('dynamodb') as dynamodb:
            await dynamodb.put_item(
                TableName=DYNAMODB_TABLE,
                Item={
                    'city': {'S': city},
                    'timestamp': {'S': timestamp},
                    's3_url': {'S': storage_url}
                }
            )
    else:
        # Log locally
        if not os.path.exists(LOCAL_LOG_FILE):
            with open(LOCAL_LOG_FILE, "w") as f:
                json.dump([], f)

        with open(LOCAL_LOG_FILE, "r") as f:
            logs = json.load(f)

        logs.append(log_entry)

        with open(LOCAL_LOG_FILE, "w") as f:
            json.dump(logs, f)
