import hashlib
import json

def normalize_data(data: dict):
    # Convert to consistent format
    normalized = {
        "user_id": str(data.get("user_id", "")).strip().lower(),
        "email": str(data.get("email", "")).strip().lower(),
        "content": str(data.get("content", "")).strip().lower()
    }
    return normalized


def generate_hash(data: dict):
    normalized = normalize_data(data)

    # Convert dict → sorted string
    data_string = json.dumps(normalized, sort_keys=True)

    # SHA256 hash
    return hashlib.sha256(data_string.encode()).hexdigest()