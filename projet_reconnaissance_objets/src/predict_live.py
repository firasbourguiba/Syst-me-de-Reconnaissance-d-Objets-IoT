import cv2
import mediapipe as mp
import joblib
import numpy as np

# Charger le modèle IA entraîné
model = joblib.load("models/sign_model.pkl")

# Initialiser MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def predict_sign_live():
    print("🖐️ Live prediction started. Show a sign. Press 'q' to quit.")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Unable to access the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error reading frame.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        predicted_letter = ""

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extraire les coordonnées x, y
                x_coords = [lm.x for lm in hand_landmarks.landmark]
                y_coords = [lm.y for lm in hand_landmarks.landmark]
                data = np.array(x_coords + y_coords).reshape(1, -1)

                # Prédiction
                predicted_letter = model.predict(data)[0]

                # Affichage dans l'image
                cv2.putText(frame, f"Prediction: {predicted_letter}", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

        cv2.imshow("Sign Language Prediction (Press 'q' to quit)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Live prediction stopped.")

if __name__ == "__main__":
    predict_sign_live()
