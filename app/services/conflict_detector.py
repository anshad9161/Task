from app.database import snapshots_collection, conflicts_collection

def detect_conflicts(patient_id, source, medications):

    previous = list(snapshots_collection.find({"patient_id": patient_id}))

    conflicts = []

    for snapshot in previous:
        for old_med in snapshot["medications"]:
            for new_med in medications:

                if old_med["name"] == new_med["name"]:

                    if old_med["dose"] != new_med["dose"]:
                        conflicts.append({
                            "patient_id": patient_id,
                            "drug": new_med["name"],
                            "conflict_type": "dose_mismatch",
                            "sources": [
                                {"source": snapshot["source"], "dose": old_med["dose"]},
                                {"source": source, "dose": new_med["dose"]}
                            ],
                            "status": "unresolved"
                        })

    if conflicts:
        conflicts_collection.insert_many(conflicts)

    return conflicts
