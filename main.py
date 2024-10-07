# saya membuat ini berdasarkan youtube video tutorial https://www.youtube.com/watch?v=RpzdQmwCJsc&list=PLcWfeUsAys2nb0i79L_LqYVfwOWEYA4eD&index=5

import json
from YT_extract import get_video_info, get_audio_url
from api import save_transcript

def save_video_sentiment(url):
    video_info = get_video_info(url)
    audio_url = get_audio_url(video_info)
    title = video_info['title']
    title = title.replace(' ', '_')
    title = "data/" + title
    save_transcript(audio_url, title, sentiment_analysis=True)


if __name__ == '__main__':
    save_video_sentiment('https://www.youtube.com/watch?v=XDfNLw1W6FA&t=122s')