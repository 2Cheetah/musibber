import youtube_dl
import json


def get_songs_metadata(urls):
    songs_metadata_dic = {}
    for url in urls:
        try:
            with youtube_dl.YoutubeDL() as ydl:
                metadata = ydl.extract_info(url, download=False)
        except:
            pass
        try:
            song_filename = metadata['artist'] +\
                ' - ' +\
                metadata['title'] +\
                '.mp3'
        except:
            song_filename = 'NA' +\
                ' - ' +\
                metadata['title'] +\
                '.mp3'
        song_filename = song_filename.replace('/', '_')
        songs_metadata_dic[song_filename] = {'url': url}
        try:
            songs_metadata_dic[song_filename]['title'] = metadata['title']
        except:
            print(f"{metadata['title']} doesn't have a title metatag")
            songs_metadata_dic[song_filename]['title'] = 'NA'
        try:
            songs_metadata_dic[song_filename]['artist'] = metadata['artist']
        except:
            print(f"{metadata['title']} doesn't have an aritst metatag")
            songs_metadata_dic[song_filename]['artist'] = ''
        try:
            songs_metadata_dic[song_filename]['album'] = metadata['album']
        except:
            print(f"{metadata['title']} doesn't have an album metatag")
            songs_metadata_dic[song_filename]['album'] = ''
        songs_metadata_dic[song_filename]['downloaded?'] = False

    with open('songs_metadata.json', 'w', encoding='utf-8') as json_file:
        json.dump(songs_metadata_dic, json_file, ensure_ascii=False)

    return songs_metadata_dic
