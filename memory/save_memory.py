import json
import os

MEMORY_FILE = "memory/history.json"


def save_candidate(candidate_data):

    # Create memory folder if not exists
    os.makedirs("memory", exist_ok=True)

    # If file doesn't exist create empty list
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)

    # Read existing history
    with open(MEMORY_FILE, "r") as f:
        try:
            history = json.load(f)
        except:
            history = []

    # Add new candidate
    history.append(candidate_data)

    # Save back to file
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=4)