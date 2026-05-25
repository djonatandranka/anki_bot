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
        print(f"Already imported: {row['Deutsch']}")
        continue

    german = row["Deutsch"]
    portuguese = row["Portugues"]
    sentence = row.get("Frase", "")
    tags = row.get("Tags", "").split(",") if row.get("Tags") else []

    if note_exists(german):
        print(f"Skipping duplicate: {german}")

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

        print(f"Added: {german}")

        added += 1

    except Exception as e:
        print(f"Error adding {german}: {e}")

sync()

send_email(added)

print(f"Added: {added}")
print(f"Skipped: {skipped}")