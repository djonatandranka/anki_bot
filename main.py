from sheets import get_rows, mark_as_imported
from anki import add_word, note_exists, sync
from emailer import send_email
import logging

rows = get_rows()

added = 0
skipped = 0

for index, row in enumerate(rows, start=2):

    imported = str(row.get("Imported", "")).strip()

    if imported == "TRUE":
        skipped += 1
        logging.info(f"Skipping already imported word: {row['Deutsch']}")
        continue

    german = row["Deutsch"]
    portuguese = row["Portugues"]
    sentence = row.get("Frase", "")
    tags = row.get("Tags", "").split(",") if row.get("Tags") else []

    if note_exists(german):
        logging.info(f"Skipping duplicate word: {german}")

        mark_as_imported(index)

        skipped += 1
        continue

    try:
        add_word(
            german=german,
            portuguese=portuguese,
            sentence=sentence,
            tags=tags
        )

        mark_as_imported(index)

        logging.info(f"Added word: {german}")

        added += 1

    except Exception as e:
        logging.error(f"Error adding {german}: {e}")

sync()

# Send email notification if any new words were added
if added > 0:
    send_email(added)

logging.info(f"Added: {added}")
logging.info(f"Skipped: {skipped}")