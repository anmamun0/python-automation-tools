import requests

access_token = 'YOUR_ACCESS_TOKEN'
video_id = 'VIDEO_ID'

url = f'https://graph.facebook.com/{video_id}?fields=source&access_token={access_token}'

response = requests.get(url)
video_url = response.json()['source']

with open('video.mp4', 'wb') as f:
    f.write(requests.get(video_url).content)
