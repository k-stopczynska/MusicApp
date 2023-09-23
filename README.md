# Music App

This is a music app that provides 2 modes: first for searching any phrase in a music database, second for recording and identify songs. App is using Shazam API.


## Features in search engine mode:

- searching for any phrase will give all the songs and artists with this phrase
- user can choose to get details on any search result
- program will offer to open a searched song in a browser

## Features in recording mode:
- program will record and encode the recording in base64 format
- while doing this program will save both raw and base64 output in a file
- as a result user will get an artist name, song title and, if possible- text of the song nicely formatted
- program will save a song in a file reverted_song_book as reverted soong text


## Installation

As there was no package manager used in this project, every dependency has to be installed manually

```bash
  pip install os, dotenv, webbrowser, requests, pyaudio, base64, time
```

os and dotenv are used to handle environmental variables, webbrowser handles opening URLs songs in a new tab, requests is sending GET ad POST requests to API, pyaudio is handling the recording in raw format, base64 is encoding it to base64 format, time manages timing in some functions with sleep method
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

Yoou can get your key subscribing on this page: https://rapidapi.com/apidojo/api/shazam


## Authors

- [@k-stopczynska](https://www.github.com/k-stopczynska)

