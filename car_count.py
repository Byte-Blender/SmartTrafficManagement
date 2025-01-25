import cv2
import cvzone
import numpy as np
from ultralytics import YOLO
import math
from sort import *



model = YOLO("../Yolo-Weights/yolov8n.pt")

classNames=  ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

def carDetect(path):
    cap = cv2.VideoCapture(path)

    tracker = Sort(max_age=20,min_hits=2,iou_threshold=0.3)

    while True:
        success, img = cap.read()
        # imgRegion = cv2.bitwise_and(img,mask)

        results = model(img, stream=True)

        detections = np.empty((0,5))

        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                # x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
                # w, h = x2 - x1, y2 - y1
                # cvzone.cornerRect(img, (x1, y1, w, h), l=10)

                # Confidence value
                conf = math.ceil((box.conf[0] * 100)) / 100
                # cvzone.putTextRect(img,f'{conf}',(max(0,x1),max(35,y1)))

                # Class names
                cls = int(box.cls[0])
                currentClass = classNames[cls]
                if currentClass == "car" and conf > 0.4:
                    # cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)), scale=0.7, thickness=1,
                    #                    offset=3)
                    # cvzone.cornerRect(img, (x1, y1, w, h), l=9)

                    currentArray = np.array([x1,y1,x2,y2,conf])
                    detections = np.vstack((detections,currentArray))



                # cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0,x1),max(35,y1)), scale=0.7,thickness=1)
        resultsTracker = tracker.update(detections)
        for result in resultsTracker:
            x1,y1,x2,y2, Id=result

            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1

            cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255,0,0))
            cvzone.putTextRect(img, f'{int(Id)}', (max(0, x1), max(35, y1)), scale=1.5, thickness=1,offset=3)

            print(result)

        cv2.imshow('image', img)

        if cv2.waitKey(0) & 0xFF == ord("q"):
            return resultsTracker[0][4]

# carDetect("cars.mp4")