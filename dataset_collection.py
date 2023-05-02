import cv2 as cv
import mediapipe as mp
import math
import csv 

f = open(r"dataset-rough.csv", 'w', newline='') #write data in csv file
writer = csv.writer(f)

i=0
cap = cv.VideoCapture(0) #start camera, 0 is the device number
hands = mp.solutions.hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)
while True:
    success, frame = cap.read()
    #cap.read() returns a boolean and an image. The boolean is stored in success
    
    frame = cv.flip(frame,1) #flip the frame around y axis
    
    results = hands.process(frame)
    
    datapoint = []
    
    if results.multi_hand_landmarks: #checks if a hand is detected
        for hand_landmark in results.multi_hand_landmarks: #for each detected hand,
            idx_to_coordinates = {}

            #gets the index and location of each landmark in the frame
            #The enumerate function is used to keep track of index while looping
            for idx, landmark in enumerate(hand_landmark.landmark):
                                                    
                #print(get_label(idx,hands,results))
                
                # print(landmark.x)
                # print(landmark.y)
                datapoint.append(landmark.x) #landmark.x is the normalized coordinate of a landmark (lies bw 0 and 1)
                datapoint.append(landmark.y)

                #frame.shape[0] is height of frame, so landmark.x * frame.shape[1] is the pixel coordinate
                #it is rounded to an integer using math.floor
                #min function ensures that calculated pixel coordinates are within the frame
                x = min(math.floor(landmark.x * frame.shape[1]), frame.shape[1] - 1)
                y = min(math.floor(landmark.y * frame.shape[0]), frame.shape[0] - 1)
                
                #store these coords
                idx_to_coordinates[idx] = x, y

                #draws a circle with center x,y radius 4 pixels color blue and -1 represents that circle should be filled in completely
                cv.circle(frame, (x,y), 4, (0,0,250), -1)

            #for ever connection bw two landmarks, draw a line joining them    
            for connection in mp.solutions.hands.HAND_CONNECTIONS:
                start_idx = connection[0]
                end_idx = connection[1]
                if start_idx in idx_to_coordinates and end_idx in idx_to_coordinates:
                    cv.line(frame, idx_to_coordinates[start_idx], idx_to_coordinates[end_idx], (0,250,0), 2)
    cv.imshow('Hands', frame)

    c = cv.waitKey(1)
    if c==ord('a'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(0)
        writer.writerow(datapoint)
    elif c==ord('b'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(1)
        writer.writerow(datapoint)
    elif c==ord('c'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(2)
        writer.writerow(datapoint)
    elif c==ord('d'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(3)
        writer.writerow(datapoint)
    elif c==ord('e'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(4)
        writer.writerow(datapoint)
    elif c==ord('f'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(5)
        writer.writerow(datapoint)
    elif c==ord('g'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(6)
        writer.writerow(datapoint)
    elif c==ord('h'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(7)
        writer.writerow(datapoint)
    elif c==ord('i'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(8)
        writer.writerow(datapoint)
    elif c==ord('j'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(9)
        writer.writerow(datapoint)
    elif c==ord('k'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(10)
        writer.writerow(datapoint)
    elif c==ord('l'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(11)
        writer.writerow(datapoint)
    elif c==ord('m'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(12)
        writer.writerow(datapoint)
    elif c==ord('n'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(13)
        writer.writerow(datapoint)
    elif c==ord('o'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(14)
        writer.writerow(datapoint)
    elif c==ord('p'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(15)
        writer.writerow(datapoint)
    elif c==ord('q'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(16)
        writer.writerow(datapoint)
    elif c==ord('r'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(17)
        writer.writerow(datapoint)
    elif c==ord('s'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(18)
        writer.writerow(datapoint)
    elif c==ord('t'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(19)
        writer.writerow(datapoint)
    elif c==ord('u'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(20)
        writer.writerow(datapoint)
    elif c==ord('v'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(21)
        writer.writerow(datapoint)
    elif c==ord('w'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(22)
        writer.writerow(datapoint)
    elif c==ord('x'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(23)
        writer.writerow(datapoint)
    elif c==ord('y'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(24)
        writer.writerow(datapoint)
    elif c==ord('z'):
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(25)
        writer.writerow(datapoint)
    elif c==32: #space
        i+=1
        print(i)
        datapoint=datapoint[:21]
        datapoint.append(26)
        writer.writerow(datapoint)
    elif c==27:
        break
    
f.close()
cap.release()
cv.destroyAllWindows()