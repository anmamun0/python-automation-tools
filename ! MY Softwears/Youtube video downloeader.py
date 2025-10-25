# YOUTUBE VIDEO DOWNLOADING WITH PYTHON AN.MAMUN0

from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=jfUdW4A8G0o'

yt = YouTube(video_url)
video = yt.streams.filter(progressive=True, file_extension='mp4',res='720p').first()
video.download('Documents')

