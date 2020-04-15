from mhmovie.youtube import yt_download
from tqdm import tqdm
import subprocess
import ffmpeg
import math
import random
import os
import glob
random.seed()


print("Cleaing up files")
files = glob.glob('./tempfiles/*.mp4')
for f in files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))
try:
    os.remove("./final.mp4")
except OSError as e:
    pass
try:
    os.remove("./video.mp4")
except OSError as e:
    pass


print("Downloading Video")
yt_download("https://www.youtube.com/watch?v=H91BxkBXttE", "video.mp4")

ffprobe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of',
                          'default=noprint_wrappers=1:nokey=1', "video.mp4"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

length = math.ceil(float((ffprobe.stdout.decode('utf-8'))))
clips = []


print("Slicing up video")
for i in tqdm(range(length)):
    # for i in tqdm(range(4)):
    task = ffmpeg.input("video.mp4", ss=i, t="1", loglevel="panic")
    task = ffmpeg.output(task, './tempfiles/video_' + str(i) + '.mp4')
    ffmpeg.run(task)
    clips.append(i)

random.shuffle(clips)

f = open("files.ffcat", "w+")
print("Creating concat file")
for clip in clips:
    f.write("file './tempfiles/video_" + str(clip) + ".mp4'\n")
f.close()

print("Creating final video")
result = subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'files.ffcat', '-c', 'copy', 'final.mp4'
                         ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print("Done")
