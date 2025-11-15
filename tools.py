# tools.py
import requests
from config import GOOGLE_API_KEY, SEARCH_ENGINE_ID

def search_space_facts(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "items" in data and len(data["items"]) > 0:
        return data["items"][0]["snippet"]
    return "Aryabot couldn't find space info for that query. Try rephrasing or asking something broader."
