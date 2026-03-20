# Medication Conflict Detection Service

A backend service that ingests medication lists from multiple clinical sources and detects potential conflicts.

This system simulates how healthcare platforms combine medication data from different systems (clinic EMR, hospital discharge, pharmacy etc.) and detect inconsistencies.

---

## Tech Stack

- Python
- FastAPI
- MongoDB
- Uvicorn

---

## Features

- Ingest medication snapshots from different sources
- Normalize medication data
- Detect medication conflicts
- Store conflicts in database
- Report unresolved conflicts

---

## API Endpoints

### 1. Ingest Medication Snapshot

POST /patients/{patient_id}/medications

Example request:

{
  "source": "clinic_emr",
  "medications": [
    {"name": "metformin", "dose": "500 mg"},
    {"name": "aspirin", "dose": "75 mg"}
  ]
}

This stores a medication snapshot and checks for conflicts with previous sources.

---

### 2. View Unresolved Conflicts

GET /reports/unresolved-conflicts

Returns all detected medication conflicts that are not resolved.

Example response:

[
  {
    "patient_id": "p1",
    "drug": "metformin",
    "conflict_type": "dose_mismatch",
    "status": "unresolved"
  }
]

---

### 3. Home Endpoint

GET /

Simple endpoint to confirm the service is running.

---

## Installation

Clone the repository:

git clone https://github.com/anshad9161/Task.git

Move into the project:

cd medication-conflict-service

Create virtual environment:

python3 -m venv venv

Activate environment:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

## Running the Server

Start MongoDB first.

Then run:

uvicorn app.main:app --reload

Server will start at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

---

## Project Structure

medication-conflict-service
│
├── app
│   ├── main.py
│   ├── database.py
│   ├── routes
│   │   ├── medications.py
│   │   └── reports.py
│   ├── services
│   │   ├── normalization.py
│   │   └── conflict_detector.py
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Author

Anshad P
