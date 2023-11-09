import cv2
import os

# Replace 'your_video.mp4' with the path to your video file.
video_path = 'your_video.mp4'
frames_folder_path = 'frames/'

# Create a VideoCapture object to read from the video file
vidcap = cv2.VideoCapture(video_path)
success, image = vidcap.read()
count = 0

# Make sure the 'frames' folder exists
if not os.path.exists(frames_folder_path):
    os.makedirs(frames_folder_path)

# Read each frame and save it as a JPEG file
while success:
    frame_file_path = os.path.join(frames_folder_path, f"frame{count}.jpg")
    cv2.imwrite(frame_file_path, image)
    success, image = vidcap.read()
    print(f'Frame {count} extracted.')
    count += 1

print(f"Extracted {count} frames.")
vidcap.release()
