import os
import webbrowser
import requests
from pprint import PrettyPrinter
from dotenv import load_dotenv
from recording import convert_raw_to_base64

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_HOST = "shazam.p.rapidapi.com"
BASE_URL = "https://shazam.p.rapidapi.com/"
AUTO_COMPLETE = "auto-complete"
SEARCH = "search"
DETECT = "songs/detect"

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
    querystring = {"term": search_param, "locale": "en-US"}
    return querystring


def get_searched_term_results():
    querystring = get_querystring("What song or artist are you looking for? ")
    songs_and_artists = get_response(BASE_URL + AUTO_COMPLETE, headers, querystring)
    records = songs_and_artists.json()["hints"]
    for record in records:
        printer.pprint(record["term"])


def open_song_url(url):
    want_open = input("Do you want me to play this song? (y/n) ").lower() == 'y'
    if want_open:
        webbrowser.open_new_tab(url)


def get_details():
    querystring = get_querystring("Which record do you want details on? ")
    data = get_response(BASE_URL + SEARCH, headers, querystring)
    songs = data.json()["tracks"]["hits"]
    for song in songs:
        title = song["track"]["title"]
        artist = song["track"]["subtitle"]
        url = song["track"]["url"]
        print(f"Title: {title}, \nArtist: {artist}, \nURL: {url}")
        open_song_url(url)


def get_details_from_recording():
    decoded_frames = convert_raw_to_base64()
    headers["content-type"] = "text/plain"
    response = requests.post(BASE_URL + DETECT, data=decoded_frames, headers=headers)
    print(response.json())

    printer.pprint(
        f"Title: {response.json()['track']['sections'][0]['metadata'][0]['text']}"
    )
    printer.pprint(
        f"Artist: {response.json()['track']['sections'][0]['metadata'][1]['text']}"
    )
    printer.pprint(f"Song text: {response.json()['track']['sections'][1]['text']}")


def main():
    # get_details_from_recording()
    get_searched_term_results()
    want_details = input("Do you want details on any search results? (y/n) ").lower() == 'y'
    if want_details :
        get_details()
    else:
        main()



if __name__ == "__main__":
    main()
