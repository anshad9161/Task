from fastapi import APIRouter
from app.database import conflicts_collection

router = APIRouter()

@router.get("/reports/unresolved-conflicts")
def get_unresolved_conflicts():

    conflicts = list(conflicts_collection.find({"status": "unresolved"}))

    for c in conflicts:
        c["_id"] = str(c["_id"])

    return conflicts
