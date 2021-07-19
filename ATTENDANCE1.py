#IMPORTING THE LIBRARIES FOR THE TEST RUN
import cv2
import numpy as np
import face_recognition
# from PIL import ImageGrab
import os
from datetime import datetime

#STORING ALL THE IAGES FROM THE FOLDER
path = 'IMAGES'
imageslist = []
classNameslist = []
myList = os.listdir(path)
print(myList)
for images in myList:
    currentImg = cv2.imread(f'{path}/{images}')
    imageslist.append(currentImg)
    classNameslist.append(os.path.splitext(images)[0])
print(classNameslist)

#ENCODING THE IMAGES 
def findEncodings(imageslist):
    encodeList = []
    for img in imageslist:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

#MARKING THE ATTENDANCE IN ATTENDANCE FILE
def markAttendance(name):
    with open("attendance-record.csv",'r+') as f:
        myDatalist = f.readlines()
        #print(myDatalist)
        nameList =[]
        for line in myDatalist:
            entry = line.split(",")
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


#FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr

encodeListKnown = findEncodings(imageslist)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

#CAPTURING IMAGES FROM WEBCAM AND ENCODING THEM
while True:
    success, img = cap.read()
    if img is None:
        print('no image captured:')
    else:
        img = cv2.resize(img, dsize=(128, 128))
        #pixels.append(img)
    # img = captureScreen()
    #imgS = cv2.resize(img, (320, 240), interpolation=cv2.INTER_AREA)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    # cap.release()
    # cv2.destroyAllWindows()

#CCOMPARING THE ENCODINGS OF WEBCAM AND IMAGES TO FIND THE MATCHINGS
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNameslist[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
           # y1, x2, y2, x1 = 4*y1, 4*x2, 4*y2, 4*x1
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cv2.putText(img, name, (x1 - 15, y2 - 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 1)
            markAttendance(name)

    screen_res = 500,500
    scale_width = screen_res[0] / img.shape[1]
    scale_height = screen_res[1] / img.shape[0]
    scale = min(scale_width, scale_height)
    # resized window width and height
    window_width = int(img.shape[1] * scale)
    window_height = int(img.shape[0] * scale)
    cv2.namedWindow('WEBCAM', cv2.WINDOW_NORMAL)
    cv2.resizeWindow("WEBCAM", window_width,window_height)

    cv2.imshow('WEBCAM', img)
    k = cv2.waitKey(1)

    if k == 27: #press esc to shutdown the webcam and stop scanning
       break

print("\n [INFO] Exiting Program and Cleanup Stuff")
cap.release()
cv2.destroyAllWindows()