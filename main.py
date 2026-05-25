from sheets import get_rows, mark_as_imported
from anki import add_word, note_exists, sync
from emailer import send_email

rows = get_rows()

added = 0
skipped = 0

for index, row in enumerate(rows, start=2):

    imported = str(row.get("Imported", "")).strip()

    if imported == "TRUE":
        skipped += 1
        print(f"Already imported: {row['German']}")
        continue

    german = row["German"]
    english = row["English"]
    sentence = row.get("Sentence", "")

    if note_exists(german):
        print(f"Skipping duplicate: {german}")

        mark_as_imported(index)

        skipped += 1
        continue

    try:
        add_word(
            deck="German",
            german=german,
            english=english,
            sentence=sentence,
            tags=["google-sheets"]
        )

        mark_as_imported(index)

        print(f"Added: {german}")

        added += 1

    except Exception as e:
        print(f"Error adding {german}: {e}")

sync()

send_email(added)

print(f"Added: {added}")
print(f"Skipped: {skipped}")