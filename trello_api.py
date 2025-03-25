import os
import requests
from dotenv import load_dotenv

load_dotenv()

TRELLO_KEY = os.getenv("TRELLO_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_LIST_ID = os.getenv("TRELLO_LIST_ID")
TRELLO_BASE_API = os.getenv("TRELLO_BASE_API")
TRELLO_BOARD_ID = os.getenv("TRELLO_BOARD_ID")

HEADERS = {
        "Accept": "application/json"
    }


def create_trello_card(name, desc) -> str:
    url = f"{TRELLO_BASE_API}/cards"

    query = {
        'idList': TRELLO_LIST_ID,
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN,
        'name': name,
        'desc': desc
    }

    response = requests.post(url, headers=HEADERS, params=query)
    response.raise_for_status()

    return response.json()


def archive_all_list_cards() -> None:
    url = f"{TRELLO_BASE_API}/lists/{TRELLO_LIST_ID}/archiveAllCards"

    query = {
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN,
    }

    response = requests.post(url, headers=HEADERS, params=query)
    response.raise_for_status()

    return response.json()

