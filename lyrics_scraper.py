#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import os
import re

# make Genius API calls
GENIUS_API_TOKEN='OPkcrzwgDB3afqREjiSjegnNFqBSzdhKDJm8LhliplJy1fJna7NzbjhlBpU7w3gl'

def get_artist_info(artist_name, page):
    '''
    Get artist object from Genius API
    '''
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response

def get_song_url(artist_name, song_cap):
    '''
    Get Genius.com song url's from artist object
    '''
    page = 1
    songs = []

    while True:
        response = get_artist_info(artist_name, page)
        json = response.json()        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)

        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)

        if (len(songs) == song_cap):
            break
        else:
            page += 1

    print('Found {} songs by {}'.format(len(songs), artist_name))
    return songs

def scrape_song_lyrics(url):
    '''
    Scrape lyrics from a Genius.com song URL
    '''
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()
    #remove identifiers like chorus, verse, etc
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
    #remove empty lines
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])         
    return lyrics

def write_lyrics_to_file(artist_name, song_count):
    f = open('lyrics/' + artist_name.lower() + '.txt', 'wb')
    urls = request_song_url(artist_name, song_count)
    for url in urls:
        lyrics = scrape_song_lyrics(url)
        f.write(lyrics.encode("utf8"))
    f.close()
    num_lines = sum(1 for line in open('lyrics/' + artist_name.lower() + '.txt', 'rb'))
    print('Wrote {} lines to file from {} songs'.format(num_lines, song_count))


def main():
    print('Requesting information from Genius.com API')
    get_song_url('The Beatles', 2)
    print('All done.')

if __name__ == '__main__':
    main()
