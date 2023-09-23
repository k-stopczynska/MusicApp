import webbrowser
from request import get_querystring
from request import get_response
from utils import BASE_URL, ENDPOINTS, headers


def get_searched_term_results():
	querystring = get_querystring("What song or artist are you looking for? ")
	songs_and_artists = get_response(
		"GET", BASE_URL + ENDPOINTS["AUTO_COMPLETE"], headers,
		querystring)
	records = songs_and_artists.json()["hints"]
	for record in records:
		print(record["term"])


def open_song_url(url):
	want_open = (input(
		"Do you want me to open this song's URL? (y/n) ").strip().lower() == 'y')
	if want_open:
		webbrowser.open_new_tab(url)


def get_song_details():
	querystring = get_querystring("Which record do you want details on? ")
	data = get_response(
		"GET", BASE_URL + ENDPOINTS['SEARCH'], headers, querystring)
	songs = data.json()["tracks"]["hits"]
	for song in songs:
		title = song["track"]["title"]
		artist = song["track"]["subtitle"]
		url = song["track"]["url"]
		print(f"Title: {title}, \nArtist: {artist}, \nURL: {url}")
		open_song_url(url)


def use_search_engine():
	get_searched_term_results()
	want_details = (input(
		"Do you want details on any search results? (y/n) ").lower() == 'y')
	if want_details:
		get_song_details()
	else:
		use_search_engine()
