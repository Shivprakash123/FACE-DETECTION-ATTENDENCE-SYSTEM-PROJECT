#IMPORTING THE LIBRARIES FOR THE TEST RUN
import cv2
import face_recognition
import numpy as np

#LOADING AND CONVERTING THE IMAGES FROM BGR TO RGB
imgMARK = face_recognition.load_image_file('IMAGES/Mark Zuckerberg.jpg')
imgMARK = cv2.cvtColor(imgMARK, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('IMAGES/Mark Test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

#ENCODING THE IMAGES
faceLoc = face_recognition.face_locations(imgMARK)[0]
encodeMark = face_recognition.face_encodings(imgMARK)[0]
cv2.rectangle(imgMARK, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

#COMPARING THE IMAGES
results = face_recognition.compare_faces([encodeMark], encodeTest)
faceDis = face_recognition.face_distance([encodeMark], encodeTest)
print(results, faceDis)
cv2.putText(imgMARK, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

#OPENING THE IMAGES
cv2.imshow('Mark Zuckerberg', imgMARK)
cv2.imshow('Mark Test', imgTest)
cv2.waitKey(0)