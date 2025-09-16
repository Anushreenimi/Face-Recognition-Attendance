import cv2
import os

url = "http://<YOUR_PHONE_IP>:8080/video"  #Enter ip shown on your webcm app

name = input("Enter your name: ")
path = f"data/images/{name}"
os.makedirs(path, exist_ok=True)

cap = cv2.VideoCapture(url)  #connect to phone camera

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Check your camera stream URL.")
        break

    cv2.imshow("Capturing Images", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imwrite(f"{path}/{count}.jpg", frame)
    count += 1
    if count >= 50:  #captures images
        break

cap.release()
cv2.destroyAllWindows()
print(f"✅ Images saved in {path}")
