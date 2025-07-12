import os
import cv2
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector   

from moviepy.video.VideoClip import TextClip, ImageClip  
from moviepy.video.compositing import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

INPUT_PATH = "data/input/"
OUTPUT_PATH = "data/output/"
HIGHLIGHT_DURATION = 10  # seconds to extract from start of each scene


def detect_scenes(video_path):
    print(f"Detecting scenes in {video_path}...")

    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=45.0))  # adjustable

    video_manager.set_downscale_factor()
    video_manager.start()

    scene_manager.detect_scenes(frame_source=video_manager)
    scene_list = scene_manager.get_scene_list()

    video_manager.release()
    print(f"Detected {len(scene_list)} scenes.")
    return scene_list


def extract_highlights(video_path, scenes, max_highlights=15):
    print("Extracting highlight clips...")

    filename = os.path.splitext(os.path.basename(video_path))[0]
    clip = VideoFileClip(video_path)
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    highlights = scenes[:max_highlights]

    for i, (start_time, end_time) in enumerate(highlights):
        start_sec = start_time.get_seconds()
        end_sec = end_time.get_seconds()

        # ✅ Skip very short scenes (e.g., under 2 seconds)
        if (end_sec - start_sec) < 4:
            continue

        subclip = clip.subclip(start_sec, end_sec)
        out_file = os.path.join(OUTPUT_PATH, f"{filename}_highlight_{i+1}.mp4")
        subclip.write_videofile(out_file, codec="libx264", audio_codec="aac", verbose=False, logger=None)

        print(f"Saved: {out_file}")



def summarize(video_file):
    full_path = os.path.join(INPUT_PATH, video_file)
    scenes = detect_scenes(full_path)
    extract_highlights(full_path, scenes)


if __name__ == "__main__":
    test_file = "videoplayback.mp4"  # Put your sample video here
    summarize(test_file)
