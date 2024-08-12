import yt_dlp

URL = 'https://www.youtube.com/watch?v=jzi6RNVEOtA'
DIR = 'C:\\Youtube'

ydl_opts = {
    'format': 'worst',
    'outtmpl': f'{DIR}/%(title)s.%(ext)s',
    'postprocessors': [{  # 音訊轉換
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # 將音訊轉換為 mp3 格式
        'preferredquality': '192',
    }],
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(URL, download=True)

        downloaded_format = next((f for f in info_dict['formats'] if f['ext'] == 'm4a'), None)
        if downloaded_format:
            downloaded_itag = downloaded_format.get("format_id", None)
            print(f"Downloaded format itag: {downloaded_itag}")
        else:
            print("Failed to retrieve itag for the downloaded format.")

    print(f"Audio downloaded successfully to{DIR}")

except Exception as e:
    print(f"非預期錯誤發生:{e}")