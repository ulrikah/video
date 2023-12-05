import cv2
from pathlib import Path

import time
import math
import argparse

def timestamp():
    return time.strftime("%Y%m%d-%H%M%S")

def frames_from_video(video_path) -> list:
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if ret:
            frames.append(frame)
        else:
            break
    return frames

def get_input_folder():
    input_folder = Path('assets/input')
    input_folder.mkdir(exist_ok=True)
    return input_folder

def get_output_folder():
    output_folder = Path('assets/output')
    output_folder.mkdir(exist_ok=True)
    return output_folder

def get_all_jpgs_in_path(folder : Path):
    return [str(f) for f in folder.glob('*.jpg')]

def save_frames(frames : list, output_folder : Path):
    t = int(time.time())
    for i, frame in enumerate(frames):
        cv2.imwrite(str(output_folder.joinpath(f"frame{str(i)}_{str(t)}.jpg")), frame)
    print(f"Saved {len(frames)} frames to {output_folder}")
    
def save_image(frame, output_path : Path):
    return cv2.imwrite(str(output_path), frame)
        
def concatenate_frames(list_2d):
    return cv2.vconcat([cv2.hconcat(list_h) for list_h in list_2d])

def resize_image(image, scale):
    height, width, _ = image.shape
    new_width = int(width * scale)
    new_height = int(height * scale)
    return cv2.resize(image, (new_width, new_height))

def sequence_to_grid(frames):
    """
    Reshape a 1D sequence of frames into a 2D square grid
    """
    dim = int(math.sqrt(len(frames)))
    image_grid = []
    row = 0
    for _ in range(dim):
        image_grid.append(frames[row * dim: (row + 1) * dim])
        row += 1
    return image_grid

def read_images_from_files(filenames):
    return [cv2.imread(f) for f in filenames]

def verify_file_path(filepath : str):
    if Path(filepath).is_file():
        return filepath
    else:
        raise IOError(f"File {filepath} does not exist")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=verify_file_path)
    return parser.parse_args()

def main():
    args = parse_args()
    # video_id = Path(args.path).stem
    video_id = Path("/Users/ulrikah/Downloads/videoer-siden-jeg-kom-til-paris/20230903_230717.mp4")
    video_path = video_id if video_id.is_file() else get_input_folder().joinpath(f"{video_id}.mp4")
    frames = frames_from_video(str(video_path))
    images = [resize_image(image, 0.1) for image in frames]
    cc = concatenate_frames(sequence_to_grid(images))
    filename = f"{video_id}-{timestamp()}.png"
    output_path = get_output_folder().joinpath(filename)
    success = save_image(cc, output_path)
    print(f"Saved {str(output_path)}") if success else print(f"Failed to save {str(output_path)}")

if __name__ == "__main__":
    main()

    