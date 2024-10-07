import yt_dlp as youtube_dl

ydl = youtube_dl.YoutubeDL()

def get_video_info(url):
    with ydl:
        result = ydl.extract_info(url, download=False)  #extract the info
        return result
    if 'entries' in result:
        return result['entries'][0]
    return result

def get_audio_url(video_info):
    for f in video_info["formats"]:
        if f["ext"] == "m4a":
            return f["url"]

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=xFFs9UgOAlE'
    video_info = get_video_info(url)
    audio_url = get_audio_url(video_info)
    print(audio_url)