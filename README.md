# Syst-me-de-Reconnaissance-d-Objets-IoT
Système de Commande Gestuelle Vocale Personnalisée
markdown
Copier
Modifier
# 🤖 Système de Commande Gestuelle Vocale Personnalisée

## 🎯 Objectif du projet

Ce projet permet à un utilisateur de contrôler des messages vocaux à l’aide de gestes personnalisés capturés via une webcam. Il est particulièrement destiné à des personnes en situation de handicap vocal pour s’exprimer simplement.

## 🧠 Fonctionnement

Le système utilise :
- 🖐️ MediaPipe pour détecter les positions des mains
- 🤖 Un modèle IA entraîné avec `scikit-learn`
- 🔊 Synthèse vocale (text-to-speech) avec `pyttsx3`
- 🌐 Une interface Flask pour interagir facilement

---

## 🧱 Architecture des fichiers

projet_reconnaissance_objets/
├── data/ # Données capturées
│ ├── gestures.csv # Données d'entraînement
│ ├── gestures_to_phrases.csv # Mappage gestes → messages vocaux
│ └── history.txt # Historique des détections
├── models/
│ └── sign_model.pkl # Modèle IA entraîné
├── src/
│ ├── collect_gestures.py # Script de collecte de gestes
│ ├── train_model.py # Entraînement du modèle
│ ├── predict_translator.py # Traduction geste → vocal
│ └── web/ # Interface Flask
│ ├── app.py # Routes Flask
│ └── templates/
│ └── index.html # Interface utilisateur
├── .gitignore
└── README.md

yaml
Copier
Modifier

---

## ⚙️ Installation

1. **Cloner le projet**
```bash
git clone <URL_DU_REPO>
cd projet_reconnaissance_objets
Créer un environnement virtuel

bash
Copier
Modifier
python -m venv .venv
source .venv/Scripts/activate  # (Windows)
Installer les dépendances

bash
Copier
Modifier
pip install -r requirements.txt
Si requirements.txt n’existe pas, installe manuellement :

bash
Copier
Modifier
pip install opencv-python mediapipe scikit-learn pyttsx3 pandas flask
🚀 Démarrage rapide
1. Collecter tes propres gestes
bash
Copier
Modifier
python src/collect_gestures.py
➡️ Enregistre un geste, puis donne-lui un nom (ex: S1, STOP, HELP)

2. Définir les messages associés
📄 Modifier le fichier :

csv
Copier
Modifier
# data/gestures_to_phrases.csv
label,message
S1,Je suis en danger
S2,Appelez à l’aide s’il vous plaît
3. Entraîner le modèle IA
bash
Copier
Modifier
python src/train_model.py
4. Lancer la prédiction avec vocalisation
bash
Copier
Modifier
python src/predict_translator.py
🧠 L’IA reconnaît ton geste → 🔊 lit le message correspondant

🌐 Optionnel : interface web (dashboard)
Lancer :

bash
Copier
Modifier
python src/web/app.py
Ouvrir dans le navigateur :
http://localhost:5000

✅ Fonctionnalités terminées
✅ Détection de gestes personnalisés

✅ Système de synthèse vocale

✅ Entraînement dynamique du modèle

✅ Interface Web (Dashboard + Statistiques + Export CSV)

✅ Réinitialisation et collecte intuitive

📊 Technologies utilisées
Python 3.10+

OpenCV / MediaPipe

Scikit-learn

pyttsx3 (offline voice)

Flask

Bootstrap + Chart.js

💡 Améliorations futures
🔁 Reconnaissance de gestes dynamiques (par mouvement)

🗂️ Interface web pour ajouter/éditer les messages

📱 Déploiement Raspberry Pi / Interface mobile

👨‍💻 Auteur
Nom : Firas
École : Ynov - B2 Informatique
Projet : Système de reconnaissance gestuelle et vocale











 Détails des bibliothèques et pourquoi elles sont nécessaires :

Bibliothèque	Utilité
opencv-python	Capture et traitement d’images
numpy	Calculs numériques (utilisé par OpenCV & AI)
tensorflow	Modèle d’IA pour la reconnaissance d’objets
torch & torchvision	PyTorch (alternative à TensorFlow pour l’IA)
flask & flask-cors	Serveur API pour communiquer avec Raspberry Pi
sqlite3	Base de données locale
pandas	Manipulation des données
matplotlib	Visualisation des données et résultats
requests	Communication avec API distante
pyyaml	Gestion des fichiers de configuration
