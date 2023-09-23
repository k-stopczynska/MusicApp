import os
from dotenv import load_dotenv
# module to load environmental variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_HOST = "shazam.p.rapidapi.com"
BASE_URL = "https://shazam.p.rapidapi.com/"
ENDPOINTS = {
    "AUTO_COMPLETE": "auto-complete",
    "SEARCH": "search",
    "DETECT": "songs/detect"}
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidApi-Host": API_HOST,
}
