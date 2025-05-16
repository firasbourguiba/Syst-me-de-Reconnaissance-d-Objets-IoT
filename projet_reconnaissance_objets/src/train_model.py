import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Charger les données
csv_path = "data/gestures.csv"
if not os.path.exists(csv_path):
    print("❌ File not found:", csv_path)
    exit()

df = pd.read_csv(csv_path)

# Vérifier qu'il y a bien des données
if df.empty:
    print("❌ gestures.csv is empty.")
    exit()

print("📄 Loaded dataset with shape:", df.shape)

# Séparer les features (X) et les labels (y)
X = df.drop("label", axis=1)
y = df["label"]

# Diviser en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner le modèle (KNN ici)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Tester le modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained with accuracy: {accuracy:.2f}")

# Sauvegarder le modèle
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/sign_model.pkl")
print("💾 Model saved to models/sign_model.pkl")
