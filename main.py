from sheets import rows
from anki import add_word, sync, note_exists
from emailer import send_email


added = 0

for row in rows:
    german = row["Deutsch"]
    portuguese = row["Portugues"]
    sentence = row.get("Frase", "")
    tags = row.get("Tags", "").split(",") if row.get("Tags") else []

    # Check if the note already exists before adding
    if not note_exists(german):
        # Add the word to Anki
        add_word(
            german=german,
            portuguese=portuguese,
            sentence=sentence,
            tags=tags
        )
        added += 1
    
    else:
        print(f"Note for '{german}' already exists. Skipping.")

sync()

# Send email notification
if added > 0:
    send_email(added)

# Print the number of words added
print(f"Added {added} words.")