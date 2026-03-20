from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import SessionLocal
from app.schemas import DataSchema
from app.services.hash_service import generate_hash
from app.services.validation_service import validate_data
from app.services.deduplication_service import is_duplicate
from app.models.data_model import Data   # ✅ FIXED IMPORT
from app.utils.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/data", status_code=201)
def add_data(data: DataSchema, db: Session = Depends(get_db)):
    try:
        # Step 1: Log incoming request
        logger.info(f"Incoming data: {data.dict()}")

        # Step 2: Validate data
        is_valid, message = validate_data(data)
        if not is_valid:
            logger.warning(f"Validation failed: {message}")
            raise HTTPException(status_code=400, detail=message)

        # Step 3: Generate hash
        data_hash = generate_hash(data.dict())
        logger.info(f"Generated hash: {data_hash}")

        # Step 4: Check duplicate
        existing_record = is_duplicate(db, data_hash)
        if existing_record:
            logger.warning("Duplicate data detected")
            return {
                "status": "duplicate",
                "message": "Data already exists",
                "existing_id": existing_record.id
            }

        # Step 5: Store new record
        new_record = Data(   # ✅ FIXED HERE
            user_id=data.user_id,
            email=data.email,
            content=data.content,
            hash=data_hash
        )

        db.add(new_record)
        db.commit()
        db.refresh(new_record)

        logger.info(f"Data stored successfully with ID: {new_record.id}")

        return {
            "status": "stored",
            "message": "Data stored successfully",
            "id": new_record.id
        }

    except HTTPException as http_err:
        raise http_err

    except SQLAlchemyError as db_err:
        db.rollback()
        logger.error(f"Database error: {str(db_err)}")

        raise HTTPException(
            status_code=500,
            detail="Database error occurred"
        )

    except Exception as e:
        db.rollback()
        logger.error(f"Unexpected error: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
@router.get("/data")
def get_all_data(db: Session = Depends(get_db)):
    try:
        records = db.query(Data).all()

        return [
            {
                "id": r.id,
                "user_id": r.user_id,
                "email": r.email,
                "content": r.content
            }
            for r in records
        ]

    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Failed to fetch data"
        )

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(Data).count()

    return {
        "total_records": total,
        "status": "healthy"
    }