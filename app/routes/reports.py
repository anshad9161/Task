from fastapi import APIRouter
from app.database import conflicts_collection

router = APIRouter()

@router.get("/reports/unresolved-conflicts")
def unresolved_conflicts():

    conflicts = list(conflicts_collection.find({"status": "unresolved"}))

    return {"conflicts": conflicts}
