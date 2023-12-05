import time
from pathlib import Path

from moviepy.editor import VideoFileClip, concatenate_videoclips

VIDEOS_DIR = Path("/Users/ulrikah/Downloads/videoer-siden-jeg-kom-til-paris/")
OUTPUT_DIR = Path(".").parent / "assets" / "output"


def timestamp():
    return time.strftime("%Y%m%d-%H%M%S")

def main():
    video_file_paths = [
        # "20230813_193344.mp4",
        # "20230813_011611.mp4",
        # "20230811_191317.mp4",
        # "20230806_170327.mp4",
        # "20230903_230717.mp4"
        "20230909_132436.mp4",
        "20230806_170327.mp4",
        "20230811_191317.mp4",
        "20230813_011611.mp4",
        "20230813_193344.mp4",
        "20230815_220819.mp4",
        "20230815_221907.mp4",
        "20230817_104734.mp4",
        "20230819_161942.mp4",
        "20230819_210748.mp4",
        "20230820_014745.mp4",
        "20230823_115123.mp4",
        "20230823_133811.mp4",
        "20230823_195409.mp4",
        "20230902_013343.mp4",
        "20230903_201726.mp4",
        "20230903_201745.mp4",
        "20230903_230717.mp4",
        "20230904_114558.mp4",
        "20230904_181225.mp4",
        "20230905_080136.mp4",
        "20230905_081511.mp4",
        "20230905_081808.mp4",
        "20230906_083558.mp4",
        "20230907_192634.mp4",
        "20230907_220232.mp4",
        "20230908_221106.mp4",
        "20230908_225042.mp4",
        "20230909_125422.mp4"
    ]
    total_seconds = 10
    seconds_per_video = total_seconds / len(video_file_paths)
    videos_to_compose = [
        VideoFileClip(str(VIDEOS_DIR / video_path)).subclip(0, seconds_per_video)
        for video_path in video_file_paths
    ]
    audios_to_compose = [video.audio for video in videos_to_compose]
    final_clip = concatenate_videoclips(videos_to_compose, method="compose")
    concatenation_filename = f"my_concatenation_{timestamp()}"
    final_clip.audio.write_audiofile(str(OUTPUT_DIR / f"{concatenation_filename}.mp3"), remove_temp=True)
    final_clip.write_videofile(str(OUTPUT_DIR / f"{concatenation_filename}.mp4"), remove_temp=True)
    print("Done")

# from moviepy.audio.AudioClip import CompositeAudioClip
#
# final_clip = concatenate_videoclips(videos_to_compose, method="compose")
# final_clip.set_audio(CompositeAudioClip([video.audio for video in videos_to_compose]))
# final_clip.write_videofile(str(OUTPUT_DIR / f"my_concatenation_{timestamp()}.mp4"), remove_temp=False)


if __name__ == '__main__':
    main()
"my_concatenation_20231206-005026.mp4"