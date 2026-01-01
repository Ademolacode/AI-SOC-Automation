REQUIRED_FIELDS = [
    "summary",
    "severity",
    "mitre",
    "recommended_actions"
]

def validate(payload: dict) -> bool:
    return all(field in payload for field in REQUIRED_FIELDS)
