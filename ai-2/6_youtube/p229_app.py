import yt_dlp

def get_youtube_video_info(video_url):
    ydl_opts = {
        'noplaylist':True,
        'quiet':True,
        'no_warnings':True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        video_id = video_info['id']
        title = video_info['title']
        upload_data = video_info['upload_date']
        channel = video_info['channel']
        duration = video_info['duration_string']
    
    return video_id, title, upload_data, channel, duration

video_url = 'https://www.youtube.com/watch?v=pSJrML-TTmI'
print(get_youtube_video_info(video_url))