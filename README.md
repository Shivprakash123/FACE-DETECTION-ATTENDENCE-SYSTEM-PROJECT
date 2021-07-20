# FACE-DETECTION-ATTENDENCE-SYSTEM-PROJECT

<h1>Desription:</h1>
In this project we are going to develop a face-recognition + attendance system which will recognize the face and diplay its name on webcam and note its attendance in a csv file. We have done the code in python language which contains some amazing libraries to detect the faces in an image. 

<h1>Libraries/Dependencies Used:</h1>
○ Numpy - a library for Python, adding support for multi-dimensional arrays and matrices, in conjunction with an enormous assortment of high-level mathematical functions to operate on these arrays.


○ Datetime - It’s a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond etc.

○ Face_Recognition - Recognize and manipulate faces from Python or the command line with the world’s simplest face recognition library.

○ OpenCV - a library of programming functions primarily geared toward real-time computer vision.

○ Dlib - C++ Library containing machine learning agorithms

○ os - a module in python which provides functions for interacting with the operation system

<h1>Understanding the code:</h1>

o BASIC1.PY FILE

  -We are first training the program to detect the faces in an image and encoding the scanned faces using face_recognition library 
  
  -Now we are testing the code to compare the encodings of the two images of the same user and see if the results are true or false
  
   [Screenshot (1919)](https://user-images.githubusercontent.com/87631649/126274047-63f03ed8-d8c6-4950-871d-b2be4a58a5f3.png)
  
o ATTENDANCE1.PY FILE 

  -Now we are creating a code to automatically load , encode all the images from the Images FOLDER and then compare it with the real-time face on web cam and note its attendance    in the csv file if the webcam face matches with the images. 
  
  
<h1>Instructions to run the code: </h1>
-First download or clone the project

-Import the project to your favourit IDE or in Pycharm

-Create an python enviroment

-Install all the packages/dependencies

-make sure the images folder path is correctly mentioned (if you have cloned then don't worry)

-Run the project using the command line or your IDE Run Button (recommended : Run in Pycharm)

-press ESC to close the webcam or terminate the code
