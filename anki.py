import requests

ANKI_URL = "http://localhost:8765"

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


def add_word(
    deck,
    german,
    portuguese,
    sentence="",
    tags=None
):
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
    return invoke("sync")