password = 'oZbob0Qk0hPEvkTO'
user = 'test_hillel_api_mailing@ukr.net'
server = 'smtp.ukr.net'

import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(
        *,
        recipients: list[str],
        mail_body: str,
        mail_subject: str,
        attachment: str = None,
):
    SERVER = server
    PASSWORD = password
    USER = user

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f'<Lection 29 user {USER}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    if attachment:
        file_exists = os.path.exists(attachment)
        if not file_exists:
            print(f"file {attachment} does not exist")
        else:
            basename = os.path.basename(attachment)
            filesize = os.path.getsize(attachment)
            file = MIMEBase('application', f'octet-stream; name={basename}')
            file.set_payload(open(attachment, 'rb').read())
            file.add_header('Content-Description', attachment)
            file.add_header('Content-Description', f'attachment; filename={attachment}; size={filesize}')
            encoders.encode_base64(file)
            msg.attach(file)

    text_to_send = MIMEText(mail_body, 'plain')
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SERVER)
    mail.login(USER, PASSWORD)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


send_email(
    recipients=['test_hillel_api_mailing@ukr.net'],
    mail_body='Some text in body',
    mail_subject='some subject',
    attachment='email_sending.py',
)
