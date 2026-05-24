from sheets import rows
from anki import add_word, sync

added = 0

for row in rows:
    german = row["Deutsch"]
    portuguese = row["Portugues"]
    sentence = row.get("Frase", "")
    tags = row.get("Tags", "").split(",") if row.get("Tags") else []

    add_word(
        deck="German",
        german=german,
        portuguese=portuguese,
        sentence=sentence,
        tags= tags
    )

    added += 1

sync()

print(f"Added {added} words.")