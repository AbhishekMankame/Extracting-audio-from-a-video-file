import imageio
imageio.plugins.ffmpeg.download()

import moviepy.editor
# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip(r"../../../...mp4")  # Entering the videofile

audio = video.audio

# Replace the parameter with the location along with filename
audio.write_audiofile(r"../../../...mp3")

print('converted successfully')


