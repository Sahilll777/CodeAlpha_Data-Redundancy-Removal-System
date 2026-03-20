from fastapi import FastAPI
from app.routes import data_routes

from app.db.database import engine
from app.models.data_model import Base

import time

app = FastAPI(title="Data Redundancy Removal System")

def wait_for_db():
    retries = 10
    while retries > 0:
        try:
            conn = engine.connect()
            conn.close()
            print("Database connected successfully")
            return
        except Exception as e:
            print("Waiting for DB...", e)
            time.sleep(2)
            retries -= 1
    raise Exception("Could not connect to database")


@app.on_event("startup")
def startup():
    wait_for_db()
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")


app.include_router(data_routes.router)


@app.get("/")
def root():
    return {"message": "Data Redundancy System API Running Successfully!"}