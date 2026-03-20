from fastapi import APIRouter
from datetime import datetime

from app.database import snapshots_collection
from app.services.normalization import normalize_medications
from app.services.conflict_detector import detect_conflicts

router = APIRouter()

@router.post("/patients/{patient_id}/medications")
def ingest_medications(patient_id: str, payload: dict):

    medications = normalize_medications(payload["medications"])

    conflicts = detect_conflicts(
        patient_id,
        payload["source"],
        medications
    )

    snapshot = {
        "patient_id": patient_id,
        "source": payload["source"],
        "medications": medications,
        "created_at": datetime.utcnow()
    }

    snapshots_collection.insert_one(snapshot)

    return {
        "message": "Medication snapshot stored",
        "conflicts_detected": len(conflicts)
    }
