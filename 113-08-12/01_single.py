import yt_dlp

URL = 'https://www.youtube.com/watch?v=jzi6RNVEOtA'
DIR = 'C:\\Youtube'

ydl_opts = {
    'format': 'worst',
    'outtmpl': f'{DIR}/%(title)s.%(ext)s',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(URL, download=True)

        video_id = info_dict.get("id", None)

        video_title = info_dict.get("title", None)

        downloaded_format_id = info_dict.get("format_id", None)

    if video_id and downloaded_format_id:
        print(f"Video'{video_title}'成功下載最低解析度")
        print(f"Video ID: {video_id}")
        print(f"Downloaded format itag: {downloaded_format_id}")

except Exception as e:
    print(f"非預期錯誤發生:{e}")