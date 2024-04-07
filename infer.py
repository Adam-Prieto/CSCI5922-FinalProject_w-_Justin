from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO("runs/detect/train/weights/best.pt") 
    results = model.predict("https://ultralytics.com/assets/african-wildlife-sample.jpg")