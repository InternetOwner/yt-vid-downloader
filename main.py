from yt_dlp import YoutubeDL


def download(urls=[]):
    url = urls[0]
    with YoutubeDL({"quiet": True}) as ydl:
        ydl.download(url)
        info = ydl.extract_info(url, download=False) # скачивание
    return {
        "title": info.get("title"),
        "duration": info.get("duration"),
        "uploader": info.get("uploader"),
        "thumbnails": info.get("thumbnails"),
        "formats": [(f["format_id"], f.get("ext"), f.get("vcodec"), f.get("acodec")) for f in info.get("formats", [])],
    }


download([input()])

