import redis

# Redis connection
redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

BLOOM_FILTER_KEY = "data_dedup"

def add_to_bloom(hash_value):
    return redis_client.execute_command("BF.ADD", BLOOM_FILTER_KEY, hash_value)

def check_bloom(hash_value):
    return redis_client.execute_command("BF.EXISTS", BLOOM_FILTER_KEY, hash_value)