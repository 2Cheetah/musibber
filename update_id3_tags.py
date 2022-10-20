import eyed3
import os
import json

# Usage example
# audiofile = eyed3.load("song.mp3")
# audiofile.tag.artist = "Token Entry"
# audiofile.tag.album = "Free For All Comp LP"
# audiofile.tag.album_artist = "Various Artists"
# audiofile.tag.title = "The Edge"
# audiofile.tag.track_num = 3
# audiofile.tag.save()


def update_id3_tags():
    with open('songs_metadata.json', 'r+') as songs_metadata_json:
        songs_metadata_dic = json.load(songs_metadata_json)

    path_to_songs = "./Music/"
    list_of_songs = os.listdir(path_to_songs)
    for song in list_of_songs:
        audiofile = eyed3.load(path_to_songs + song)
        audiofile.tag.title = songs_metadata_dic[song]['title']
        audiofile.tag.artist = songs_metadata_dic[song]['artist']
        audiofile.tag.album = songs_metadata_dic[song]['album']
        audiofile.tag.save()
