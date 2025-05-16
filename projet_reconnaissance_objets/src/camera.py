import os
import cv2

def capture_image():
    print("🚀 Image capture started...")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Unable to open the camera!")
        return

    print("📸 Press SPACE to capture an image, or 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error: Unable to read the frame!")
            break

        cv2.imshow('Camera - SPACE to capture, Q to quit', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord(' '):  # SPACE key
            save_dir = "data/images"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            img_path = os.path.join(save_dir, "capture.png")
            cv2.imwrite(img_path, frame)
            print("✅ Image successfully captured and saved.")

        elif key == ord('q'):  # Q key to quit
            break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Image capture ended.")
    print("📁 Image saved in the folder: data/images/capture.png")


if __name__ == "__main__":
    capture_image()