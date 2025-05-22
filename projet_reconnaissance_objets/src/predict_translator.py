import cv2
import mediapipe as mp
import joblib
import numpy as np
import pyttsx3
import pandas as pd
import time

# Charger le modèle
model = joblib.load("models/sign_model.pkl")

# Charger la table des traductions
mapping = pd.read_csv("data/gestures_to_phrases.csv")
translation_dict = dict(zip(mapping["label"], mapping["message"]))

# Initialiser la synthèse vocale
tts = pyttsx3.init()

# Initialiser MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def predict_translation_live():
    print("🧠 Mode traducteur gestuel activé. Faites un signe...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Webcam non détectée.")
        return

    last_label = ""
    cooldown = 3  # temps d'attente entre deux messages (en secondes)
    last_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        predicted_label = ""
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
                predicted_label = prediction

        # Affichage
        cv2.putText(frame, f"Geste: {predicted_label} ({confidence:.2f})", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        if predicted_label and confidence > 0.8 and predicted_label != last_label:
            now = time.time()
            if now - last_time > cooldown:
                phrase = translation_dict.get(predicted_label)
                if phrase:
                    print(f"🗣️ Traduction : {phrase}")
                    tts.say(phrase)
                    tts.runAndWait()
                    last_label = predicted_label
                    last_time = now

        cv2.imshow("🧠 Traducteur Gestes → Voix", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Fermeture du traducteur.")

if __name__ == "__main__":
    predict_translation_live()
