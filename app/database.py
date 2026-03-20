from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["medication_db"]

patients_collection = db["patients"]
snapshots_collection = db["medication_snapshots"]
conflicts_collection = db["conflicts"]
