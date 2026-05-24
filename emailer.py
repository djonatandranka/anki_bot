import smtplib
from email.message import EmailMessage

def send_email(count):
    msg = EmailMessage()
    msg["Subject"] = "Anki Updated"
    msg["From"] = "you@gmail.com"
    msg["To"] = "wife@gmail.com"

    msg.set_content(f"{count} new German words added.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("you@gmail.com", "APP_PASSWORD")
        smtp.send_message(msg)