import youtube_dl
import os
import json


def check_downloaded_songs():
    with open('songs_metadata.json', 'r+') as songs_metadata_json:
        songs_metadata_dic = json.load(songs_metadata_json)

    path_to_songs = "./Music/"
    list_of_songs = os.listdir(path_to_songs)
    for song in list_of_songs:
        try:
            songs_metadata_dic[song]['downloaded?'] = True
        except:
            pass

    with open('songs_metadata.json', 'w', encoding='utf-8') as json_file:
        json.dump(songs_metadata_dic, json_file, ensure_ascii=False)


def download_songs(urls):
    filename_pattern = "./Music/%(artist)s - %(title)s.%(ext)s"

    ydl_opts = {
        'outtmpl': filename_pattern,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'}]
    }

    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # ydl.download(urls)
    for url in urls:
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            pass
