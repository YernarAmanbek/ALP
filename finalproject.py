import cv2 as cv
import numpy as nm

# Video record
cap = cv.VideoCapture(0)

# Setting a frame size for the program
cap.set(cv.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 800)

# Path for file
weights = "models\\yolo3\\yolov3.weights"
cfgFile = "models\\yolo3\\yolo3.cfg"
classFile = "models\\yolo3classes.txt"

# Loading Yolo...
net = cv.dnn.readNet(weights, cfgFile)

# Reading and inputing classes from the file to the list
with open(classFile, "r") as f:
    classes = [apple.strip() for apple in f.readlines()]

# Get layers from the network
layer_names = net.getLayerNames()

# Output layers | .getUnconnectedOutLayers() returns indices of layers
output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

# Yolo status in the case of success
print("Yolo working fine:)")

# is.Opened returns boolean. Checks for the camera's work
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame | .read() - boolean
    ret, frame = cap.read()
    frame = cv.resize(frame, None, fx=1, fy=1)
    height, width, channels = frame.shape

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame. BREAK!")
        break

    # blob, so we can change the frame and pass it to the CNN
    blob = cv.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)

    #Object detection
    net.setInput(blob)
    outputs = net.forward(output_layers)

    class_ids = []
    confidences = []
    confidences1 = []
    boxes = []
    for out in outputs:
        for detection in out:
            # Giving a score for detected objects
            scores = detection[5:]
            class_id = nm.argmax(scores)
            confidence = scores[class_id]
            confidence_score = []
            # If confidence in recognizing is higher than 0.5, create coordinates, so after we can make rectangles
            if confidence > 0.8:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                confidences1.append(confidence)
        # We use NMS function in opencv to perform Non-maximum Suppression
        # we give it score threshold and nms threshold as arguments.
        indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv.FONT_HERSHEY_COMPLEX
        colors = nm.random.uniform(200, 255, size=(len(classes), 3))
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                labelPercent = str(confidences1[i])
                color = colors[class_ids[i]]
                cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv.putText(frame, label, (x, y + 30), font, 1, color, 2)
                cv.putText(frame, labelPercent, (x, y + 50), font, 1, color, 2)

    # Our operations on the frame come here
    frame1 = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)


    # Display the resulting frame
    cv.imshow('YOLO | SAMARATIN', frame1)

    # Terminate the process by pressing "q"
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()