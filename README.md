# Face-Recognition-Attendance
Face recognition system using Python, OpenCV and Raspberrypi
### Table of Contents-
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Project Structure](#project-structure)
4. [Set-up Instructions](#set-up-instructions)
     1. [Install required libraries](#install-required-libraries)
     2. [Capture Dataset](#capture-dataset)
     3. [Train model](#train-model)
     4. [Run Attendance](#run-attendance)
5. [Output](#output)
## Features
* Capture face images for multiple users using a phone camera.
* Train a face recognition model with the LBPH algorithm.
* Real-time face recognition and automatic attendance logging.
* Attendance stored in a CSV file with timestamps.
## Technologies Used
* Python 3
* OpenCV
* NumPy
* face-recognition
* Raspberry Pi (supports mobile IP Webcam)
## Project Structure
Face Recognition Attendance

* dataset.py        #captures images from phone camera
* train.py          #trains the LBPH face recognizer
* attendance.py     #recognizes face and logs attendance
* attendance.csv    #stores attendance logs(auto-generated)
* dataset/          #folder to store the captured images
## Set-up Instructions
### Install required libraries
open the raspberry pi terminal and run
```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install opencv-python opencv-contrib-python numpy pillow
```
### Capture Dataset
run the dataset script to capture images
```bash
python3 dataset.py
```
### Train model
```bash
python3 train.py
```
### Run Attendance
Run the attendance script for live recognition
```bash
python2 attendace.py
```
## Output
* Live video feed with recognized names displayed
```bash
attendence.csv logs attendance
```





