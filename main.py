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

def get_querystring(search_term):
    search_param = input(search_term)
    querystring = {'term': search_param, 'locale': 'en-US'}
    return querystring


def get_searched_term_results():
    querystring = get_querystring("What song or artist are you looking for? ")
    songs_and_artists = get_response(BASE_URL + AUTO_COMPLETE, headers, querystring)
    records = songs_and_artists.json()['hints']
    for record in records:
        printer.pprint(record['term'])


def get_details():
    querystring = get_querystring("Which record do you want details on? ")
    songs = get_response(BASE_URL + SEARCH, headers, querystring)
    for song in songs.json()['tracks']['hits']:
        title = song['track']['title']
        artist = song['track']['subtitle']
        url = song['track']['url']
        print(f"Title: {title}, Artist: {artist}, URL: {url}")


def main():
    get_searched_term_results()
    want_details = input("Do you want details on any search results? (y/n)")
    if want_details :
        get_details()
    else:
        get_searched_term_results()


if __name__ == "__main__":
    main()