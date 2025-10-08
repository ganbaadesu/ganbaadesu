from moviepy.editor import *
import hashlib
import os

for x in os.listdir():
    if x.endswith(".mp4"):
        name = (hashlib.md5((x.replace(".mp4", "")).encode())).hexdigest()
        video = VideoFileClip(x)
        video.audio.write_audiofile(name+".mp3")
