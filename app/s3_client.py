import asyncio
import json
import os
from datetime import datetime
from app.config import AWS_S3_BUCKET, USE_AWS, LOCAL_STORAGE_PATH
from aiobotocore.session import get_session


async def upload_to_storage(city: str, data: dict):
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{city}_{timestamp}.json"
    local_path = os.path.join(LOCAL_STORAGE_PATH, filename)

    # Save data locally
    with open(local_path, "w") as f:
        json.dump(data, f)

    if USE_AWS:
        # Use AWS S3 for storage
        session = get_session()
        async with session.create_client('s3') as s3:
            await s3.upload_file(local_path, AWS_S3_BUCKET, filename)
        # Return the S3 URL
        return f"s3://{AWS_S3_BUCKET}/{filename}"
    else:
        # Return the local path
        return local_path
