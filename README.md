# 🤖 CV Matcher – L'agent RH intelligent basé sur l'IA (Gratuit & Open Source)

Bienvenue dans **CV Matcher**, un assistant RH intelligent propulsé par l'IA (Gemini).  
Cet outil vous permet de :

- 📥 Uploader plusieurs CV au format PDF  
- 🧠 Les analyser automatiquement avec l'intelligence artificielle  
- 🔎 Poser une requête ("je cherche un profil Python avec 2 ans d'expérience")  
- 🎯 Obtenir les meilleurs candidats selon vos besoins

Le tout, gratuitement, en local, via une interface simple (Gradio).

---

## 🚀 Démo rapide

*Lancer une recherche, visualiser les résultats, en un clic.*

---

## ⚙️ Fonctionnalités

- 🧾 Lecture automatique des CV (PDF)
- ✨ Extraction des données structurées avec Google Gemini
- 🧠 Matching intelligent avec vos besoins RH
- 🖥️ Interface web claire avec Gradio
- 💾 Résultats enregistrés en `.json` dans le dossier `/CV`

---

## 📦 Installation

### 1. Cloner le repo
```bash
git clone https://github.com/votre-user/cv-matcher.git
cd cv-matcher
```

### 2. Créer un environnement virtuel
```bash
python -m venv env
source env/bin/activate  # sous Windows: env\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Ajouter votre clé API Gemini
Créez un fichier `.env` ou modifiez `config.py` avec :

```python
GEMINI_API_KEY = "votre_clé_API_GEMINI"
```

> 🔑 Vous pouvez obtenir une clé sur https://makersuite.google.com/app

---

## ▶️ Lancer l'application

```bash
python app.py
```

L’interface Gradio s’ouvrira automatiquement dans votre navigateur.

---

## 📁 Organisation du projet

```bash
cv-matcher/
│
├── app.py                  # Interface Gradio principale
├── main.py                 # Traitement des PDF et analyse Gemini
├── config.py               # Chemins & clés API
├── llm/
│   ├── generate_json.py    # Parsing des CV via Gemini
│   └── matcher.py          # Matching selon une requête
├── utils/
│   └── io.py               # Chargement des fichiers JSON
├── data/pdf/               # 📥 PDF CV déposés ici
├── CV/                     # 📤 Résultats JSON enregistrés ici
└── requirements.txt
```

---

## 🧠 Exemple de requête

```txt
Je cherche un Data Scientist avec de l'expérience en finance, Python et Power BI.
```

L'agent IA retournera :
- ✅ Le nom des candidats correspondants
- ⭐️ Un score de similarité
- 📌 Une explication de la correspondance

---

## 💬 Besoin d’aide ?

Si vous n’arrivez pas à faire fonctionner l’outil, que l’installation vous bloque, ou que vous avez une question :

👉 **Écrivez-moi, je vous aiderai avec plaisir.**  
Vous pouvez m’envoyer un message sur LinkedIn ou ouvrir une issue ici sur GitHub.

---

## 📌 À venir

- 🌐 Version en ligne hébergée (Cloud)

---

## 🧑‍💻 Auteur

Développé par [**Mehdi Zemmam**](https://www.linkedin.com/in/zemmam-mehdi/)  
Passionné d'IA, NLP, data science & automatisation intelligente.

---
