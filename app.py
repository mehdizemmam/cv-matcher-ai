# app.py

import os
import gradio as gr
from config import PDF_DIR
from llm.generate_json import analyze_cv_with_gemini_and_save
from llm.matcher import match_profiles
from utils.io import load_all_cv

# 📁 Créer les dossiers nécessaires
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs("data/cv", exist_ok=True)

# 🔄 1. Fonction de parsing des fichiers
def handle_upload(files):
    messages = []
    for file in files:
        filename = os.path.basename(file.name)
        save_path = os.path.join(PDF_DIR, filename)
        with open(file.name, "rb") as src, open(save_path, "wb") as dst:
            dst.write(src.read())
        result = analyze_cv_with_gemini_and_save(save_path)
        messages.append(f"✅ `{filename}` analysé avec succès.")
    return "\n".join(messages)

# 🔍 2. Fonction de recherche
def query_profiles(user_query):
    cvs = load_all_cv()
    if not cvs:
        return "⚠️ Aucun CV JSON disponible. Veuillez en ajouter d'abord."
    response = match_profiles(user_query, cvs)
    return response if response else "❌ Aucun profil ne correspond à votre demande."

# 🎨 Interface utilisateur Gradio
with gr.Blocks(title="CV Matcher RH — by Mehdi Zemmam", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
# 🤖 Assistant Recruteur IA — *CV Matcher*
Une solution complète pour automatiser l'analyse de CVs et trouver les meilleurs candidats grâce à **Gemini**.

**Étapes simples :**
1. Uploadez un ou plusieurs CVs PDF  
2. Posez une question RH (ex: _Je cherche un Data Analyst avec 2 ans d’expérience en finance_)

---
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## 📤 Upload & Parsing des CVs")
            file_input = gr.File(
                file_types=[".pdf"],
                file_count="multiple",
                label="Sélectionnez vos fichiers PDF",
                interactive=True
            )
            upload_button = gr.Button("🚀 Analyser les CVs avec Gemini")
            upload_output = gr.Textbox(
                label="Résultat du parsing",
                lines=10,
                max_lines=20,
                show_copy_button=True
            )
            upload_button.click(fn=handle_upload, inputs=[file_input], outputs=[upload_output])

        with gr.Column(scale=1):
            gr.Markdown("## 🔎 Recherche de Candidats")
            user_question = gr.Textbox(
                placeholder="Ex: Je cherche un profil data senior maîtrisant Python",
                label="Décrivez votre besoin",
                lines=3,
                max_lines=5
            )
            search_button = gr.Button("🎯 Trouver les meilleurs profils")
            search_output = gr.Textbox(
                label="Résultat de l’analyse de profils",
                lines=12,
                max_lines=20,
                show_copy_button=True
            )
            search_button.click(fn=query_profiles, inputs=[user_question], outputs=[search_output])

    gr.Markdown(
        """
---

### 💼 À propos
Développé par Mehdi Zemmam | Powered by [Gemini API](https://ai.google.dev/)

> _CV Matcher IA est une interface conçue pour simplifier le recrutement en combinant parsing intelligent et recommandation IA._
        """,
        elem_id="footer"
    )

# ▶️ Lancer l'app
if __name__ == "__main__":
    demo.launch()
