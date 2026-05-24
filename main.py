from sheets import rows
from anki import add_word, sync
from emailer import send_email

added = 0

for row in rows:
    german = row["Deutsch"]
    portuguese = row["Portugues"]
    sentence = row.get("Frase", "")
    tags = row.get("Tags", "").split(",") if row.get("Tags") else []

    add_word(
        german=german,
        portuguese=portuguese,
        sentence=sentence,
        tags=tags
    )

    added += 1

sync()

# Send email notification
send_email(added)

# Print the number of words added
print(f"Added {added} words.")