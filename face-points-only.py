import dlib
import cv2
import numpy as np
import os

# Load the pre-trained face detector and facial landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Function to detect faces and draw facial landmarks with different colors for each feature
def detect_and_draw_colored_landmarks(input_path, output_folder, background_color=(255, 255, 255)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the image
    image = cv2.imread(input_path)
    height, width, _ = image.shape  # Get image dimensions

    # Create a new image with the specified background color
    new_image = np.full((height, width, 3), background_color, dtype=np.uint8)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(gray)

    # Define colors for different facial features (in BGR format)
    eye_color = (0, 255, 0)   # Green
    nose_color = (0, 0, 255)   # Red
    mouth_color = (255, 0, 0)  # Blue

    # Loop through each face and draw facial landmarks with different colors for each feature
    for idx, face in enumerate(faces):
        landmarks = predictor(gray, face)

        # Draw landmarks on the new image with different colors for each feature
        for i in range(68):
            x, y = landmarks.part(i).x, landmarks.part(i).y

            # Assign colors based on facial feature
            if 36 <= i <= 47 or 17 <= i <= 26:  # Points for eyes
                color = eye_color
            elif 48 <= i <= 67:  # Points for mouth
                color = mouth_color
            else:  # Points for nose and other facial features
                color = nose_color

            cv2.circle(new_image, (x, y), 5, color, -1)  # Decreased circle size for better visibility

    # Save the new image with facial landmarks in the output folder
    output_path = os.path.join(output_folder, os.path.basename(input_path))
    cv2.imwrite(output_path, new_image)

# Process all images in the "faces" folder and save results in "faces-colored-points" folder
input_folder = "faces"
output_folder = "faces-points-only"
background_color = (255, 255, 255)  # Set your desired background color (BGR format)

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        detect_and_draw_colored_landmarks(input_path, output_folder, background_color)
