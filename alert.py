import cv2
import dlib
import time
import pygame
from scipy.spatial import distance as dist

# Function to calculate eye aspect ratio (EAR)
def get_eye_aspect_ratio(eye):
    # Convert the landmarks to a list of (x, y) tuples
    eye_points = [(point.x, point.y) for point in eye]
    
    # Calculate the Euclidean distances between the vertical and horizontal eye landmarks
    vertical_dist1 = dist.euclidean(eye_points[1], eye_points[5])
    vertical_dist2 = dist.euclidean(eye_points[2], eye_points[4])
    horizontal_dist = dist.euclidean(eye_points[0], eye_points[3])
    
    # Compute the EAR (Eye Aspect Ratio)
    ear = (vertical_dist1 + vertical_dist2) / (2.0 * horizontal_dist)
    return ear

# Initialize the camera
cap = cv2.VideoCapture(0)

# Load the face detector and landmark predictor models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Initialize pygame for sound
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound('su.wav')  # Replace with the path to your alarm sound file

# Variables to track blinks and the time eye is closed
eye_closed_start_time = None  # To track the time when the eyes are closed
eye_closed_duration = 3 # 5 seconds threshold for eye closure

while True:
    # Capture frame-by-frame from the camera
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = detector(gray)
    
    for face in faces:
        # Get landmarks
        landmarks = predictor(gray, face)
        
        # Get the eye landmarks (index 36 to 41 for the left eye, 42 to 47 for the right eye)
        left_eye = [landmarks.part(i) for i in range(36, 42)]
        right_eye = [landmarks.part(i) for i in range(42, 48)]
        
        # Calculate the eye aspect ratio (EAR) for blink detection
        left_eye_ratio = get_eye_aspect_ratio(left_eye)
        right_eye_ratio = get_eye_aspect_ratio(right_eye)
        
        # Check if the eyes are closed (EAR below a threshold)
        if left_eye_ratio < 0.2 and right_eye_ratio < 0.2:
            if eye_closed_start_time is None:
                # Start tracking time when the eye first closes
                eye_closed_start_time = time.time()
            else:
                # Check if the eye has been closed for more than 5 seconds
                elapsed_time = time.time() - eye_closed_start_time
                if elapsed_time >= eye_closed_duration:
                    # Play the alarm sound if the eyes are closed for 5 seconds
                    alarm_sound.play()
                    cv2.putText(frame, "Alert", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        else:
            # Reset the timer if the eyes are open
            eye_closed_start_time = None
        
    # Display the resulting frame
    cv2.imshow("Eye Blink Detection", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
