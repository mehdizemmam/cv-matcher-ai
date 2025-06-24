# utils/io.py

import os
import json
import re
from config import CV_JSON_DIR

def save_json_result(response_text):
    try:
        data = json.loads(response_text)
    except Exception:
        print("❌ Gemini did not return valid JSON.")
        return

    os.makedirs(CV_JSON_DIR, exist_ok=True)

    first = re.sub(r"\W+", "", data.get("first_name", "Unknown")).capitalize()
    last = re.sub(r"\W+", "", data.get("last_name", "Unknown")).capitalize()
    filename = f"{CV_JSON_DIR}/{last}{first}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ CV saved as {filename}")

def load_all_cv():
    cvs = []
    for file in os.listdir(CV_JSON_DIR):
        if file.endswith(".json"):
            with open(os.path.join(CV_JSON_DIR, file), "r", encoding="utf-8") as f:
                cv = json.load(f)
                cv["__file__"] = file
                cvs.append(cv)
    return cvs
