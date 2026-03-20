def normalize_medications(medications):
    normalized = []

    for med in medications:
        normalized.append({
            "name": med["name"].strip().lower(),
            "dose": med["dose"].strip().lower()
        })

    return normalized
