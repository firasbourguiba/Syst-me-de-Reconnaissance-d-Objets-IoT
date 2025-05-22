from flask import Flask, render_template
from collections import Counter
from flask import Response


import subprocess
import os

app = Flask(__name__)

def run_script(script_name):
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", script_name))
    subprocess.Popen(["start", "cmd", "/k", f"python {script_path}"], shell=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_yolo")
def run_yolo():
    run_script("detection_yolo_video.py")
    return "✅ Détection d’objet (YOLOv8) lancée dans un terminal."

@app.route("/run_collect")
def run_collect():
    run_script("collect_gestures.py")
    return "✋ Collecte des gestes lancée."

@app.route("/run_train")
def run_train():
    run_script("train_model.py")
    return "🧠 Entraînement du modèle lancé."

@app.route("/run_predict")
def run_predict():
    run_script("predict_live.py")
    return "🔤 Prédiction en direct lancée."

@app.route("/stats")
def show_stats():
    history_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "history.txt"))

    stats = {}
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            letters = f.read().splitlines()
            stats = dict(Counter(letters))

    stats = dict(sorted(stats.items()))  # trier alphabétiquement
    return render_template("stats.html", stats=stats)
@app.route("/reset_stats")
def reset_stats():
    history_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "history.txt"))
    open(history_file, "w").close()  # Vide le fichier
    return "✅ Statistiques réinitialisées. <a href='/stats'>Retour aux stats</a>"

@app.route("/export_csv")
def export_csv():
    history_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "history.txt"))
    stats = {}
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            from collections import Counter
            stats = dict(Counter(f.read().splitlines()))

    csv_data = "Lettre,Détections\n"
    for letter, count in stats.items():
        csv_data += f"{letter},{count}\n"

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=statistiques.csv"}
    )

if __name__ == "__main__":
    app.run(debug=True)
