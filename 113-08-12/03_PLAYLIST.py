import yt_dlp

PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLit5T88BJDAG7MHJYj3aycHjGmD6h-xyo'
DIR = 'C:\\Youtube'

ydl_opts = {
    'format': 'worst',
    'outtmpl': f'{DIR}/%(title)s.%(ext)s',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.downloaded([PLAYLIST_URL])
    print(f"Playlist downloaded ")

except Exception as e:
    print(f"An unexpected error occurred:{e}")    