import os
import requests
from dotenv import load_dotenv
from pprint import PrettyPrinter
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_HOST = "shazam.p.rapidapi.com"
BASE_URL = "https://shazam.p.rapidapi.com/"
AUTO_COMPLETE = 'auto-complete'
SEARCH = 'search'

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidApi-Host": API_HOST,
}
printer = PrettyPrinter()

def get_response(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    return response


def get_searched_term_results():
    searched_term = input("What song are you looking for? ")
    querystring = {'term': searched_term, 'locale': 'en-US'}
    songs_and_artists = get_response(BASE_URL + AUTO_COMPLETE, headers, querystring)
    records = songs_and_artists.json()['hints']
    for record in records:
        printer.pprint(record['term'])


def get_song_details():
    searched_song = input("Which song do you want details on? ")
    querystring = {'term': searched_song, 'locale': 'en-US'}
    songs = get_response(BASE_URL + SEARCH, headers, querystring)
    for song in songs.json()['tracks']['hits']:
        title = song['track']['title']
        artist = song['track']['subtitle']
        url = song['track']['url']
        print(f"Title: {title}, Artist: {artist}, URL: {url}")


def main():
    get_searched_term_results()
    get_song_details()


if __name__ == "__main__":
    main()