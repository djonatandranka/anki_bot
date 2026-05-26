import logging
import requests
from pathlib import Path

logging.basicConfig(
    filename="anki_bot.log",
    level=logging.INFO
)

ANKI_URL = "http://localhost:8765"
CONFIG_PATH = Path(__file__).parent / "config.yaml"

def invoke(action, **params):
    response = requests.post(
        ANKI_URL,
        json={
            "action": action,
            "version": 6,
            "params": params
        }
    ).json()

    if response.get("error"):
        raise Exception(response["error"])

    return response["result"]


def load_config():
    config = {}
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.split("#", 1)[0].strip()
            if not line:
                continue
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            config[key.strip()] = value.strip()
    return config


def get_config_value(key, default=None):
    config = load_config()
    return config.get(key, default)

def note_exists(german):
    result = invoke(
        "findNotes",
        query=f'Deutsch:"{german}"'
    )

    return len(result) > 0


def add_word(
    deck=None,
    german=None,
    portuguese=None,
    sentence="",
    tags=None
):
    if deck is None:
        deck = get_config_value("deck_name")
    if not deck:
        raise ValueError("deck name must be provided either in the call or in config.yaml using deck_name")

    if tags is None:
        tags = []

    note = {
        "deckName": deck,
        "modelName": "Vocabulario_Deutsch",
        "fields": {
            "Deutsch": german,
            "Portugues": portuguese,
            "Frase": sentence
        },
        "tags": tags
    }

    return invoke("addNote", note=note)




def sync():
    try:
        result = invoke("sync")

        logging.info("Anki sync completed successfully.")

        return True

    except Exception as e:
        logging.error(f"Anki sync failed: {e}")

        return False