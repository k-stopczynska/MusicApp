import os
import requests
from dotenv import load_dotenv
from pprint import PrettyPrinter
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_HOST = "shazam.p.rapidapi.com"
BASE_URL = "https://shazam.p.rapidapi.com/auto-complete"
# querystring = {'term': 'beautiful', 'locale': 'en-US'}
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-Rapid-Api-Host": API_HOST,
}
printer = PrettyPrinter()

def get_searched_term():
    searched_term = input("What song or artist are you looking for? ")
    return searched_term

def get_response(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    return response


def main():
    search = get_searched_term()
    querystring = {'term': search, 'locale': 'en-US'}
    songs_and_artists = get_response(BASE_URL, headers, querystring)
    records = songs_and_artists.json()['hints']
    printer.pprint(songs_and_artists.json()['hints'])
    for record in records:
        printer.pprint(record['term'])


if __name__ == "__main__":
    main()