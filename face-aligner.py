import os
import cv2
import dlib
import numpy as np

def align_and_zoom_with_rotation(image_path, output_path, target_size=2000, zoom_factor=1.3, background_color=(0, 0, 0)):
    # Load the image
    img = cv2.imread(image_path)
    
    # Initialize the face detector
    face_detector = dlib.get_frontal_face_detector()
    
    # Load the facial landmarks predictor
    predictor_path = "shape_predictor_68_face_landmarks.dat"
    landmark_predictor = dlib.shape_predictor(predictor_path)
    
    # Detect faces in the image
    faces = face_detector(img, 1)

    if len(faces) != 1:
        print("Skipping", image_path, "because it does not have exactly one face.")
        return

    # Assume there is only one face in each image for simplicity
    face = faces[0]

    # Get the facial landmarks
    landmarks = landmark_predictor(img, face)

    # Calculate the angle for rotation (assuming eyes' landmarks are at positions 36 and 45)
    angle = np.degrees(np.arctan2(landmarks.part(45).y - landmarks.part(36).y, landmarks.part(45).x - landmarks.part(36).x))

    # Rotate the image around the center
    center_x = (landmarks.part(45).x + landmarks.part(36).x) // 2
    center_y = (landmarks.part(45).y + landmarks.part(36).y) // 2

    rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, 1.0)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=background_color)

    # Calculate the size of the square region of interest
    roi_size = int(max(face.width(), face.height()) * zoom_factor)

    # Calculate the coordinates of the top-left corner of the ROI to keep it centered
    roi_x = max(0, center_x - roi_size // 2)
    roi_y = max(0, center_y - roi_size // 2)

    # Extract the ROI from the rotated image
    roi = rotated_img[roi_y:roi_y + roi_size, roi_x:roi_x + roi_size]

    # Resize the ROI to the target size
    resized_img = cv2.resize(roi, (target_size, target_size))

    # Save the zoomed, aligned, and rotated image
    cv2.imwrite(output_path, resized_img)

# Input and output folders
input_folder = "input"
output_folder = "faces"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        align_and_zoom_with_rotation(input_path, output_path, target_size=2000, zoom_factor=1.7)
