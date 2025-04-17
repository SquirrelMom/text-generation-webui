import smtplib, ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PSWRD')

message = """\
Subject: Email wysłany z GitHub Actions workflow

Uwaga! Nie znaleziono pliku CMD_FLAGS!
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)                    #login
    server.sendmail(USERNAME, USERNAME, message)        #send email "from me to me"
