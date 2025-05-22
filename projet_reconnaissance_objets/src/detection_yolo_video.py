import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects_live():
    print("📷 YOLOv8 Live Object Detection Started (press 'q' to quit)")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Unable to open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error: Failed to grab frame.")
            break

        results = model.predict(source=frame, conf=0.5, verbose=False)
        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 - Object Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 YOLOv8 Detection Stopped.")

if __name__ == "__main__":
    detect_objects_live()
