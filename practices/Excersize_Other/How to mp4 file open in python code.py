# You need to install this module 
# pip install pygame
# pip install moviepy

import pygame
from moviepy.editor import *

clip = VideoFileClip('video_file.mp4')
clip.preview()
 
pygame.quit()


# if you want to resize this gui video page so you can change 8 line by
# clip = VideoFileClip('video_file.mp4').resize((600, 300))
