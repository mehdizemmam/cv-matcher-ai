# config.py

import os

# ✅ Clé API Gemini (met ta vraie clé ici ou utilise une variable d'environnement)
GEMINI_API_KEY = os.getenv("yourapikey", "yourapikey")

# 📁 Chemin vers le dossier contenant les fichiers PDF
PDF_DIR = "data/pdf"

# 📁 Dossier où seront stockés les CV transformés en JSON
CV_JSON_DIR = "data/cv"
