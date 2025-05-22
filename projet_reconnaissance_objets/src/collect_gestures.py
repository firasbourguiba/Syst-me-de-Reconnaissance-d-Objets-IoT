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
    print("✋ Mode collecte de gestes personnalisés activé.")
    print("➡️ Appuie sur ESPACE pour capturer un geste.")
    print("➡️ Tape un label personnalisé (ex: S1, AIDE, ALERTE...) puis Entrée.")
    print("➡️ Appuie sur 'q' pour quitter.")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Erreur : caméra non accessible.")
        return

    # Ouvrir (ou créer) le fichier CSV
    file_exists = os.path.isfile(save_path)
    with open(save_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            headers = [f"x{i}" for i in range(21)] + [f"y{i}" for i in range(21)] + ["label"]
            writer.writerow(headers)

        while True:
            success, frame = cap.read()
            if not success:
                print("❌ Erreur : lecture impossible.")
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.imshow("🖐️ Collecte de gestes personnalisés", frame)
            key = cv2.waitKey(1) & 0xFF

            # ESPACE → capturer les coordonnées
            if key == 32:
                if results.multi_hand_landmarks:
                    landmarks = results.multi_hand_landmarks[0]
                    x_coords = [lm.x for lm in landmarks.landmark]
                    y_coords = [lm.y for lm in landmarks.landmark]
                    label = input("✏️ Nom du geste (ex: S1, AIDE, ALERTE) : ").strip().upper()
                    print("✏️ Enter the letter for this gesture (ex: A, B...): ", end='')
                    if label:
                        writer.writerow(x_coords + y_coords + [label])
                        print(f"✅ Geste enregistré sous : {label}")
                    else:
                        print("⚠️ Label vide. Ignoré.")

            elif key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Fin de la collecte.")

if __name__ == "__main__":
    collect_data()
