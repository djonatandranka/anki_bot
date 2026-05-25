import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open("Palavras-Anki").get_worksheet(0)


def get_rows():
    return sheet.get_all_records()


def mark_as_imported(row_number):
    IMPORTED_COLUMN = 4

    sheet.update_cell(
        row_number,
        IMPORTED_COLUMN,
        "TRUE"
    )