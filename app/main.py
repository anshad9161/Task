from fastapi import FastAPI
from app.routes import medications, reports

app = FastAPI(title="Medication Conflict Service")

app.include_router(medications.router)
app.include_router(reports.router)

@app.get("/")
def home():
    return {"message": "Medication Conflict Service Running"}
