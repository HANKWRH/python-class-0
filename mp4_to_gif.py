from moviepy.editor import VideoFileClip

in_file = 'video.mp4'
out = 'video.gif'

clip = VideoFileClip(in_file)
clip.write_gif(out)