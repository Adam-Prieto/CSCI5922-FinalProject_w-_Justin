from ultralytics import YOLO


if __name__ == '__main__':
    # Load a model
    model = YOLO("yolov8m.yaml")  # build a new model from scratch
    #model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Use the model
    results = model.train(data='african-wildlife.yaml', epochs=100, imgsz=640, pretrained=False)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
    path = model.export()  # export the model to torchscript format
