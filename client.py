import argparse
import socket
import smtplib
from email.mime.text import MIMEText

#action de depart.
x = input('1. se connecter \n'
          '2. Creer un compte')

if x == 1:
    #...

else:
    #...

#envoie courriel.

rcptto = input('Rcpt to : ')
subject = input('Subject')

print('Data : ')
text = ""
temp = input()
while temp != ".":
    text += temp + "\n"
    temp = input()

msg = MIMEText(text)
#msg["From"] = client.adresse
msg['To'] = rcptto
msg['Subject'] = subject


