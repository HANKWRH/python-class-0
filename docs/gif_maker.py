from moviepy.editor import VideoFileClip
movie_input_file = 'vidio.mp4'
output_gif_file = 'boom.gif'

clip = VideoFileClip(movie_input_file)
clip.write_gif(output_gif_file)