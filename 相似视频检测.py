
# Import necessary libraries
import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
from skimage.metrics import peak_signal_noise_ratio as compare_psnr

# Define function to extract first frame of video
def extract_first_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()
    return frame

# Define function to compare similarity of two frames
def compare_frames(frame1, frame2):
    # Convert frames to grayscale
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # Calculate structural similarity index (SSIM) between frames
    if abs(gray1.shape[0]/gray1.shape[1] - gray2.shape[0]/gray2.shape[1]) < 0.5:
        gray2 = cv2.resize(gray2, (gray1.shape[1], gray1.shape[0]))
    try:
        ssim = compare_ssim(gray1, gray2)
    except:
        ssim = 0
    return ssim

# Define function to compare similarity of all videos in a directory
def compare_videos(directory):
    # Get list of all video files in directory
    video_files = [f for f in os.listdir(directory) if f.endswith('.mp4')]
    # Extract first frame of each video
    frames = [extract_first_frame(os.path.join(directory, f)) for f in video_files]
    # Compare similarity of all pairs of frames
    similarities = np.zeros((len(frames), len(frames)))
    for i in range(len(frames)):
        for j in range(i+1, len(frames)):
            similarities[i,j] = compare_frames(frames[i], frames[j])
    # Print out pairs of videos with similarity greater than a threshold
    threshold = 0.9
    for i in range(len(frames)):
        for j in range(i+1, len(frames)):
            if similarities[i,j] > threshold:
                print('相似程度{}: {} {}'.format(similarities[i,j], video_files[i], video_files[j]))

# Call compare_videos function on directory of videos
compare_videos(r'E:\车\同人3D\Bengugu')