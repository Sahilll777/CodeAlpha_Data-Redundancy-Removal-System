# Data Redundancy Removal System

A cloud-ready backend system that detects, prevents, and removes duplicate data entries using **hashing, validation, and Redis-based optimization.

This project ensures data integrity, performance, and scalability in modern cloud applications.

---

## Features

*  Data Validation – Ensures incoming data is correct and structured
*  Smart Hashing (SHA-256) – Normalizes and hashes data for accurate comparison
*  Duplicate Detection – Uses Redis (Bloom Filter) + PostgreSQL verification
*  Prevents Redundant Data – Only unique records are stored
*  Analytics API – Get system stats and stored data
*  Dockerized Setup – Easy deployment and consistent environment
*  Logging System – File + console logging with rotation

---

## Tech Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Backend          | FastAPI                 |
| Database         | PostgreSQL              |
| Cache            | Redis (Bloom Filter)    |
| ORM              | SQLAlchemy              |
| Containerization | Docker + Docker Compose |
| Language         | Python                  |

---

## Project Structure

```
data-redundancy-system/
│
├── backend/
│   ├── app/
│   │   ├── db/
│   │   │   └── database.py
│   │   │
│   │   ├── models/
│   │   │   └── data_model.py
│   │   │
│   │   ├── routes/
│   │   │   └── data_routes.py
│   │   │
│   │   ├── services/
│   │   │   ├── hash_service.py
│   │   │   ├── validation_service.py
│   │   │   ├── deduplication_service.py
│   │   │   └── redis_service.py
│   │   │
│   │   ├── utils/
│   │   │   └── logger.py
│   │   │
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── wait-for-db.sh
│
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## Setup Instructions (Local)

### 1️ Clone Repository

```
git clone <your-repo-url>
cd data-redundancy-system
```

---

### 2️ Run Using Docker

```
docker-compose up --build
```

---

### 3️ Access API

Open in browser:

```
http://localhost:8000/docs
```

---

## API Endpoints

### ➤ Add Data

**POST** `/data`

#### Request Body:

```json
{
  "user_id": "1",
  "email": "test@example.com",
  "content": "Hello World"
}
```

#### Response:

```json
{
  "status": "stored",
  "message": "Data stored successfully",
  "id": 1
}
```

---

### ➤ Duplicate Case

```json
{
  "status": "duplicate",
  "message": "Data already exists",
  "existing_id": 1
}
```

---

### ➤ Get All Data

**GET** `/data`

---

### ➤ Get System Stats

**GET** `/stats`

```json
{
  "total_records": 5,
  "status": "healthy"
}
```

---

## How It Works

1. Incoming data is validated
2. Data is normalized (case-insensitive, trimmed)
3. SHA-256 hash is generated
4. Redis Bloom Filter checks for duplicates (fast)
5. PostgreSQL confirms duplicates (accuracy)
6. Only unique data is stored

---

## Key Highlights

* Prevents duplicate entries efficiently
* Handles large-scale data using caching
* Reduces database load
* Designed for cloud-native environments

---

## Logging

* Logs stored in: `backend/logs/app.log`
* Includes:

  * Incoming requests
  * Validation failures
  * Duplicate detection
  * Errors

---

## Testing

Use Swagger UI:

```
http://localhost:8000/docs
```

Test flow:

1. Add new data → Stored
2. Add same data → Duplicate detected

---

## Author

Sahil Bhosale
Cloud & DevOps Enthusiast

---

## Contribution

Feel free to fork, improve, and contribute!

---
