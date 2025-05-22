import cv2
import mediapipe as mp
import joblib
import numpy as np
import pyttsx3
import os

# Charger le modèle
model = joblib.load("models/sign_model.pkl")

# Initialiser la synthèse vocale
tts = pyttsx3.init()

# Initialiser MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def predict_sign_live():
    print("🖐️ Show a sign. SPACE = valider lettre, ENTER = prononcer mot, BACKSPACE = effacer, Q = quitter")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Webcam non détectée.")
        return

    history = ""
    last_letter = ""
    history_file = "data/history.txt"
    os.makedirs("data", exist_ok=True)  # Crée le dossier si besoin

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        predicted_letter = ""
        confidence = 0.0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                x_coords = [lm.x for lm in hand_landmarks.landmark]
                y_coords = [lm.y for lm in hand_landmarks.landmark]
                data = np.array(x_coords + y_coords).reshape(1, -1)

                prediction = model.predict(data)[0]
                probabilities = model.predict_proba(data)[0]
                confidence = max(probabilities)
                predicted_letter = prediction

        # Affichage
        cv2.putText(frame, f"Prediction: {predicted_letter} ({confidence:.2f})", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.putText(frame, f"Word: {history}", (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

        cv2.imshow("Sign Language Prediction", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        elif key == 32:  # ESPACE
            if predicted_letter and confidence > 0.8 and predicted_letter != last_letter:
                history += predicted_letter
                last_letter = predicted_letter
                print(f"✅ Lettre ajoutée : {predicted_letter}")

                # Enregistrement dans le fichier pour les stats
                with open(history_file, "a") as f:
                    f.write(predicted_letter + "\n")

        elif key == 13:  # ENTER
            if history:
                print(f"🔊 Prononciation du mot : {history}")
                tts.say(history)
                tts.runAndWait()
                history = ""  # Réinitialiser le mot
                last_letter = ""  # Réinitialiser aussi
        elif key == 8:  # BACKSPACE
            history = ""
            last_letter = ""
            print("🗑️ Mot effacé.")

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Fermeture.")

if __name__ == "__main__":
    predict_sign_live()
