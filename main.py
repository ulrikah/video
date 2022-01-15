import cv2
from pathlib import Path
import matplotlib.pyplot as plt

import time


def frames_from_video(video_path) -> list:
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        # cv2.imwrite("frame%d.jpg" % ret, frame)     # save frame as JPEG file      
        if ret:
            frames.append(frame)
        else:
            break
    return frames

def get_io_folders():
    input_folder = Path('assets/input')
    output_folder = Path('assets/output')
    input_folder.mkdir(exist_ok=True)
    output_folder.mkdir(exist_ok=True)
    return input_folder, output_folder

def save_frames(frames : list, output_folder : Path):
    t = int(time.time())
    for i, frame in enumerate(frames):
        cv2.imwrite(str(output_folder.joinpath(f"frame{str(i)}_{str(t)}.jpg")), frame)
    print(f"Saved {len(frames)} frames to {output_folder}")
    

def main():
    input_folder, output_folder = get_io_folders()
    video_path = input_folder.joinpath('big_buck_bunny_720p_5mb.mp4')
    frames = frames_from_video(str(video_path))
    save_frames(frames, output_folder)

    

if __name__ == "__main__":
    main()

    