from ultralytics import YOLO

model = YOLO("../ModelsAndResults/yoloFrozenTrain/weights/best.pt")
model.conf = 0.557
model.predict("test6.mp4", save=True, save_txt=True, show_labels=False)
