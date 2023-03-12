from ultralytics import YOLO

model = YOLO("yolov8m_custom.pt")

model.predict(source="wr1.jpeg", show=True, save=True, conf=0.5)
