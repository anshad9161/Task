from fastapi import APIRouter
from app.database import snapshots_collection
from datetime import datetime

router = APIRouter()

@router.post("/patients/{patient_id}/medications")
def ingest_medications(patient_id: str, payload: dict):

    snapshot = {
        "patient_id": patient_id,
        "source": payload["source"],
        "medications": payload["medications"],
        "created_at": datetime.utcnow()
    }

    snapshots_collection.insert_one(snapshot)

    return {"message": "Medication snapshot stored"}
