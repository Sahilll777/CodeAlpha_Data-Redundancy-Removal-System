from app.services.redis_service import check_bloom, add_to_bloom
from app.models.data_model import Data

def is_duplicate(db, data_hash):
    # Step 1: Fast check (Redis)
    if check_bloom(data_hash):
        # Step 2: Confirm in DB (avoid false positive)
        existing = db.query(Data).filter(Data.hash == data_hash).first()
        if existing:
            return existing

    # Step 3: Not duplicate → add to Redis
    add_to_bloom(data_hash)

    return None