import cv2
import mediapipe as mp
import csv
import os

# Initialiser MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Chemin vers le fichier CSV
save_path = "data/gestures.csv"
os.makedirs("data", exist_ok=True)

def collect_data():
    print("✋ Gesture collector started.")
    print("➡️ Press SPACE to capture a gesture.")
    print("➡️ Type the corresponding letter and press ENTER.")
    print("➡️ Press 'q' to quit.")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Cannot open camera.")
        return

    # Ouvrir (ou créer) le fichier CSV
    file_exists = os.path.isfile(save_path)
    with open(save_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            # Écrire les en-têtes si le fichier est vide
            headers = [f"x{i}" for i in range(21)] + [f"y{i}" for i in range(21)] + ["label"]
            writer.writerow(headers)

        while True:
            success, frame = cap.read()
            if not success:
                print("❌ Error reading frame.")
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.imshow("Gesture Collector (SPACE to save, q to quit)", frame)
            key = cv2.waitKey(1) & 0xFF

            # Espace = capturer les données
            if key == 32:  # espace
                if results.multi_hand_landmarks:
                    landmarks = results.multi_hand_landmarks[0]
                    x_coords = [lm.x for lm in landmarks.landmark]
                    y_coords = [lm.y for lm in landmarks.landmark]
                    print("✏️ Enter the letter for this gesture (ex: A, B...): ", end='')
                    label = input().strip().upper()
                    if label.isalpha() and len(label) == 1:
                        writer.writerow(x_coords + y_coords + [label])
                        print(f"✅ Gesture saved for letter: {label}")
                    else:
                        print("⚠️ Invalid input. Please enter one letter only.")

            elif key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Gesture collection finished.")

if __name__ == "__main__":
    collect_data()
