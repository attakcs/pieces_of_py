# Simple Mail Transfer Protocol library
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Satoshi Nakamoto'
email['to'] = 'user@gmail.com'
email['subject'] = 'Store of Energy'
email.set_content(html.substitute({'fname': 'John', 'lname': 'Doe'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('**Your email**', '**Password**')
    smtp.send_message(email)
    print('All good boss!')