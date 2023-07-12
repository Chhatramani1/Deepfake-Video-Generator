# Import necessary libraries
import cv2
import dlib
import numpy as np
from imutils import face_utils

# Load the pre-trained face detection model
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load the video clip and celebrity face image
video = cv2.VideoCapture("input_video.mp4")
celebrity_face = cv2.imread("celebrity_face.jpg")

# Iterate through each frame of the video
while True:
    ret, frame = video.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    for face in faces:
        # Predict facial landmarks
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        # Extract the region of interest (ROI) from the frame
        (x, y, w, h) = face_utils.rect_to_bb(face)
        roi = frame[y:y + h, x:x + w]
        
        # Resize the celebrity face to match the size of the ROI
        celebrity_face_resized = cv2.resize(celebrity_face, (w, h))

        # Perform the face swap
        mask = np.zeros_like(roi)
        mask[y:y + h, x:x + w] = 255
        blended = cv2.seamlessClone(celebrity_face_resized, roi, mask, (x + w // 2, y + h // 2), cv2.NORMAL_CLONE)

        # Replace the ROI with the blended image
        frame[y:y + h, x:x + w] = blended

    # Display the resulting frame
    cv2.imshow("Deepfake", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close all windows
video.release()
cv2.destroyAllWindows()
