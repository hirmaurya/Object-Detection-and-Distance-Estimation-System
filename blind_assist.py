import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Camera not detected")
    exit ()
while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    results = model(frame)

    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        cls_id = int(box.cls[0])
        object_name = model.names[cls_id]

        center_x = (x1 + x2) // 2

        if center_x < w // 3:
            direction = "LEFT"
        elif center_x < 2 * w // 3:
            direction = "CENTER"
        else:
            direction = "RIGHT"

        box_width = x2 - x1

        if box_width > w * 0.4:
            distance = "1 meter"
        elif box_width > w * 0.2:
            distance = "2 meters"
        else:
            distance = "3+ meters"

        # Label
        label = f"{object_name} - {direction} - {distance}"

        # Draw box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 0, 255), 2)

    cv2.imshow("Blind Assist System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()