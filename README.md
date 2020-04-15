# frankensteins_video
Slice up a youtube video into a real monster!



Ok, so this python script will take a youtube video, download it, slice it into 1 second clips and then combine those back in random order.

To use this you will need ffmpeg.exe and ffprobe.exe in the same directory you run the script.

Also, you need the mhmovie, tqdm, & ffmpeg-python libraries.


To run it, just edit the youtube link on line 30 to whatever video you want to chop up.  

The result will end up as final.mp4 in the same directory.

It will clean up after itself except for the final video.
