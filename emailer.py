import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")
    

def send_email(count):
    msg = EmailMessage()

    msg["Subject"] = "Anki Vocabulary Updated"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_TO

    msg.set_content(
        f"{count} Novas palavras foram adicionadas ao Anki."
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)