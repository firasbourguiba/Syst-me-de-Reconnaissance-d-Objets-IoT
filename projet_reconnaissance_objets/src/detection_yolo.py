import cv2
import mediapipe as mp
import os
from datetime import datetime

# Initialiser MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

def detect_hands():
    print("🖐️ Starting hand detection... Press SPACE to save image, 'q' to quit.")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Unable to access the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error: Cannot read the camera frame.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # Dessiner les landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Affichage du flux vidéo
        cv2.imshow("Hand Detection (SPACE to save, Q to quit)", frame)
        key = cv2.waitKey(1) & 0xFF

        # Sauvegarde de l'image avec ESPACE
        if key == ord(' '):
            save_dir = "data/images"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            img_path = os.path.join(save_dir, f"sign_{timestamp}.png")
            cv2.imwrite(img_path, frame)
            print(f"✅ Image saved: {img_path}")

        # Quitter avec 'q'
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Hand detection stopped.")

if __name__ == "__main__":
    detect_hands()
