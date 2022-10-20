import get_urls_from_html
import get_songs_metadata
import download_songs
import update_id3_tags


def main():
    soup = get_urls_from_html.get_soup_from_html()
    urls = get_urls_from_html.get_urls_from_soup(soup=soup)
    get_songs_metadata.get_songs_metadata(urls=urls)
    download_songs.download_songs(urls=urls[100:150])
    update_id3_tags.update_id3_tags()


if __name__ == '__main__':
    main()
