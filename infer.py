from ultralytics import YOLO

model = YOLO("Models\yolov8n-pose.pt")

results = model.predict(source=0, show=True)