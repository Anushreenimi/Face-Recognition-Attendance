import cv2
import face_recognition
import os
import numpy as np
import pandas as pd
from datetime import datetime

# Enter your phone IP camera URL
# Example: "http://192.168.1.5:8080/video"
url = "http://<YOUR_PHONE_IP>:8080/video"

# Load known faces from the dataset
path = "data/images"
known_encodings, names = [], []

for person in os.listdir(path):
    for file in os.listdir(f"{path}/{person}"):
        img = face_recognition.load_image_file(f"{path}/{person}/{file}")
        encoding = face_recognition.face_encodings(img)
        if encoding:
            known_encodings.append(encoding[0])
            names.append(person)

# Attendance file
attendance_file = "attendance.csv"
if not os.path.exists(attendance_file):
    pd.DataFrame(columns=["Name", "Time"]).to_csv(attendance_file, index=False)

# Start camera
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Could not access phone camera. Check IP and network.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, locations)

    for encode, loc in zip(encodings, locations):
        matches = face_recognition.compare_faces(known_encodings, encode)
        face_dist = face_recognition.face_distance(known_encodings, encode)
        match_index = np.argmin(face_dist)

        if matches[match_index]:
            name = names[match_index]
            y1, x2, y2, x1 = loc
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Mark attendance only once per day
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            today = now.strftime("%Y-%m-%d")

            df = pd.read_csv(attendance_file)
            if not ((df["Name"] == name) & (df["Time"].str.contains(today))).any():
                new_entry = pd.DataFrame([[name, timestamp]], columns=["Name", "Time"])
                df = pd.concat([df, new_entry], ignore_index=True)
                df.to_csv(attendance_file, index=False)
                print(f"✅ Attendance marked for {name} at {timestamp}")

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
