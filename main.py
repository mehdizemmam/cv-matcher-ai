# main.py

import os
from config import PDF_DIR
from llm.generate_json import analyze_cv_with_gemini_and_save
from llm.matcher import match_profiles
from utils.io import load_all_cv

def parse_all_pdfs():
    print("📥 Traitement des fichiers PDF...\n")

    # 🛠️ Créer le dossier PDF si manquant
    if not os.path.exists(PDF_DIR):
        os.makedirs(PDF_DIR)
        print(f"📂 Le dossier '{PDF_DIR}' a été créé. Place tes fichiers .pdf dedans.")
        return

    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"⚠️ Aucun fichier PDF trouvé dans {PDF_DIR}")
        return

    for file in pdf_files:
        pdf_path = os.path.join(PDF_DIR, file)
        analyze_cv_with_gemini_and_save(pdf_path)

def launch_matching():
    user_input = input("\n🔎 Décris le profil recherché (ex. : Data + Python + finance):\n> ")
    cvs = load_all_cv()

    if not cvs:
        print("⚠️ Aucun CV JSON disponible dans le dossier 'data/cv'.")
        return

    print("\n🤖 Gemini analyse les profils pour vous...\n")
    results_text = match_profiles(user_input, cvs)

    if results_text:
        print("\n🎯 Profils recommandés :\n")
        print(results_text)

if __name__ == "__main__":
    print("🚀 Assistant Recruteur IA\n")
    parse_all_pdfs()
    launch_matching()
