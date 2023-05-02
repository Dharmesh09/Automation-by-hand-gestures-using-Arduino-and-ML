import cv2 as cv
import mediapipe as mp
import math
import tensorflow as tf
import serial

serialcomm = serial.Serial('COM5', 9600)

cap = cv.VideoCapture(0)
hands = mp.solutions.hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)
model = tf.keras.models.load_model('model.h5')
while True:
    success, frame = cap.read()
    results = hands.process(frame)
    datapoint = []
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            idx_to_coordinates = {}
            for idx, landmark in enumerate(hand_landmark.landmark):
                datapoint.append(landmark.x)
                datapoint.append(landmark.y)
                x = min(math.floor(landmark.x * frame.shape[1]), frame.shape[1] - 1)
                y = min(math.floor(landmark.y * frame.shape[0]), frame.shape[0] - 1)
                idx_to_coordinates[idx] = x, y
                cv.circle(frame, (x,y), 4, (0,0,250), -1)
            for connection in mp.solutions.hands.HAND_CONNECTIONS:
                start_idx = connection[0]
                end_idx = connection[1]
                if start_idx in idx_to_coordinates and end_idx in idx_to_coordinates:
                    cv.line(frame, idx_to_coordinates[start_idx], idx_to_coordinates[end_idx], (0,250,0), 2)
    frame = cv.flip(frame, 1)
    datapoint=datapoint[:21]
    try:
        pred = model.predict([datapoint])
        # print(pred)
        val = pred.argmax(axis=1)[0]
        print(val)
        # serialcomm.write(val)
        if val==0:
            serialcomm.write(str.encode('0'))
        elif val==1:
            serialcomm.write(str.encode('1'))
        elif val==2:
            serialcomm.write(str.encode('2'))
        elif val==3:
            serialcomm.write(str.encode('3'))
        elif val==4:
            serialcomm.write(str.encode('4'))
    except:
        pass
    cv.imshow('window', frame)
    c = cv.waitKey(1)
    if c==27:
        try:
            serialcomm.write(str.encode('4'))
        except:
            pass
        break

cap.release()
cv.destroyAllWindows()