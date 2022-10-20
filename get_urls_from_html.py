from bs4 import BeautifulSoup


def get_soup_from_html():
    path_to_html = input("Relative route to the folder with .html file: ")
    path_to_html += "/YouTube Music.html"
    with open(path_to_html, encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
    return soup


def get_urls_from_soup(soup):
    urls = []
    urls_raw = []
    a_tags = soup.find_all(
        'a',
        class_="yt-simple-endpoint style-scope yt-formatted-string"
    )
    for a_tag in a_tags:
        urls_raw.append(a_tag.get('href'))
    for url in urls_raw:
        if 'watch' in url:
            urls.append(url[:url.find('&')])
    return urls
