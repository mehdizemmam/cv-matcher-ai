# llm/generate_json.py

import os
import re
import json
import google.generativeai as genai
from parser.extract_cv import extract_text_from_pdf
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def build_prompt(cv_text):
    return f"""
You are a resume parser. Given the raw unstructured resume text below, extract the following information in valid and clean JSON format:

- first_name
- last_name
- email
- phone
- skills (list of strings)
- education (list of objects with degree, institution, year)
- experience (list of objects with title, company, duration)
- languages (list of strings)

Here is the resume content:
\"\"\"
{cv_text}
\"\"\"

Return only valid JSON, with no explanation, markdown, or formatting. 
The output must start with '{{' and end with '}}'. Do not say anything else.
"""

def analyze_cv_with_gemini_and_save(pdf_path, output_dir="data/cv"):
    cv_text = extract_text_from_pdf(pdf_path)

    if not cv_text.strip():
        print(f"⚠️ PDF vide ou non textuel : {pdf_path}")
        return

    prompt = build_prompt(cv_text)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    print(f"🤖 Analyse de : {os.path.basename(pdf_path)}")
    response = model.generate_content(prompt)

    raw_text = response.text.strip()

    # 🧹 Extraire proprement le JSON
    json_start = raw_text.find("{")
    json_end = raw_text.rfind("}")
    if json_start != -1 and json_end != -1:
        raw_text = raw_text[json_start:json_end+1]

    try:
        data = json.loads(raw_text)
    except Exception as e:
        print("❌ JSON parsing failed. Raw response was:\n")
        print(response.text)
        return

    os.makedirs(output_dir, exist_ok=True)

    first = re.sub(r"\W+", "", data.get("first_name", "Unknown")).capitalize()
    last = re.sub(r"\W+", "", data.get("last_name", "Unknown")).capitalize()
    filename = os.path.join(output_dir, f"{last}{first}.json")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"✅ JSON saved as: {filename}")
