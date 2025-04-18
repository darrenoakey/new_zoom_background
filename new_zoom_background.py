#!python
import os
import json
import random
import subprocess

zoom_backgrounds_dir = "/Users/darrenoakey/Movies/zoom backgrounds/"
scenes_file = "/Users/darrenoakey/Library/Application Support/obs-studio/basic/scenes/Untitled.json"
applescript_file = (
    "/Users/darrenoakey/Library/Application Support/obs-studio/basic/scenes/obs_virtual_camera.applescript"
)
current_background_file = 'current_background.txt'


def kill_obs():
    subprocess.run(["killall", "OBS"])


def pick_random_background():
    backgrounds = [
        f for f in os.listdir(zoom_backgrounds_dir) if f.lower().endswith(".mp4") or f.lower().endswith(".mov")
    ]
    return random.choice(backgrounds)


def replace_background_in_dynamic_video(new_background):
    with open(scenes_file, "r") as f:
        data = json.load(f)

    for source in data["sources"]:
        if source["name"] == "dynamic_video":
            source["settings"]["local_file"] = os.path.join(zoom_backgrounds_dir, new_background)
    with open(scenes_file, "w") as f:
        json.dump(data, f)


def save_current_background(new_background):
    with open(current_background_file, 'w') as f:
        f.write(new_background)


def start_obs_with_virtual_camera():
    subprocess.run(["osascript", applescript_file])


if __name__ == "__main__":
    kill_obs()
    new_background = pick_random_background()
    replace_background_in_dynamic_video(new_background)
    save_current_background(new_background)
    start_obs_with_virtual_camera()
