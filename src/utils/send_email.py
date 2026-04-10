import yagmail
import os

yag = yagmail.SMTP('samchlystek20@gmail.com', password=os.environ.get('GMAIL_APP'))

def send_warning_email(subject: str, body: str):
    yag.send(
        to='samchlystek20@gmail.com',
        subject=subject,
        contents=body
    )

