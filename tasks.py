from huey import RedisHuey
import redis
import json

# Initialize Huey with Redis backend
huey = RedisHuey()

# Redis connection
red = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
print("conecction->>>>>")
@huey.task()
def store_key_value_to_redis(key, value):
    # Check if value is not a str or bytes, then serialize it to JSON
    if not isinstance(value, (str, bytes)):
        value = json.dumps(value)
    red.set(key, value)

@huey.task()
def retrieve_value_from_redis(key):
    # Retrieve value from Redis
    value = red.get(key)
    try:
        # Try to deserialize from JSON, fall back to original value if it fails
        value = json.loads(value)
    except (TypeError, json.JSONDecodeError):
        pass
    return value
@huey.task()
def delete_key_from_redis(key):
    # Delete the key from Redis
    result = red.delete(key)
    return result > 0  # Returns True if the key was deleted, False otherwise
