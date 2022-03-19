import cv2
from pathlib import Path
from matplotlib import image
import matplotlib.pyplot as plt

import time
import math


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
    
def concatenate_frames(list_2d):
    return cv2.vconcat([cv2.hconcat(list_h) for list_h in list_2d])

def sequence_to_grid(frames):
    """
    Reshape a 1D sequence of frames into a 2D square grid
    """
    # TODO: resize all frames to a certain size
    dim = int(math.sqrt(len(frames)))
    image_grid = []
    row = 0
    for _ in range(dim):
        image_grid.append(frames[row * dim: (row + 1) * dim])
        row += 1
    return image_grid

def read_files(filenames):
    return [cv2.imread(f) for f in filenames]

def main():
    # SAVE VIDEO TO FRAMES
    # input_folder, output_folder = get_io_folders()
    # video_path = input_folder.joinpath('big_buck_bunny_720p_5mb.mp4')
    # frames = frames_from_video(str(video_path))
    # save_frames(frames, output_folder)[]



    # CONCATENATE FRAMES FROM DISK
    input_folder, output_folder = get_io_folders()
    filenames = [str(f) for f in output_folder.glob('*.jpg')]
    files = read_files(filenames)
    cc = concatenate_frames(sequence_to_grid(files))
    plt.imshow(cc)
    plt.show()
   

if __name__ == "__main__":
    main()

    