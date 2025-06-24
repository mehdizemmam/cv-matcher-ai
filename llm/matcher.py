# llm/matcher.py

import json
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def build_matching_prompt(user_request, cvs):
    prompt = f"""
Tu es un assistant recruteur intelligent.

L'utilisateur cherche un candidat correspondant à la description suivante :

\"\"\"
{user_request}
\"\"\"

Tu vas analyser une liste de profils (format JSON) et identifier ceux qui **correspondent vraiment au besoin**. Si aucun ne convient, dis-le clairement.

Règles importantes :
- Ne propose aucun profil s’il ne correspond pas
- Si un candidat est légèrement pertinent, indique un score faible
- Si aucun ne correspond, écris : "❌ Aucun candidat ne correspond à ce profil."

Pour chaque bon profil, donne une réponse en français clair :

👤 Nom : <Nom complet>  
⭐️ Score de correspondance : <xx>%  
📌 Raisons : <Pourquoi ce candidat correspond>

Voici les profils :
"""

    for cv in cvs:
        prompt += f"\n\nCandidat :\n{json.dumps(cv, indent=2)}"

    return prompt

def match_profiles(user_request, cvs):
    prompt = build_matching_prompt(user_request, cvs)
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Erreur lors de l'appel à Gemini :", e)
        return None
