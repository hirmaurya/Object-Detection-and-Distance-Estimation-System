from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # nano model (lightweight)

results = model("https://ultralytics.com/images/bus.jpg")

print("YOLO working successfully")
