# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:29:36 2020

@author: Dawson
"""

import os

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from emil import Encoders

gmail_user = "dtemail098@gmail.com"
gmail_pwd = "gmailAccount1"
to = "djtorch123@gmail.com, tocarchid5@students.rowan.edu"
subject = "Wave File Test"
text = "Hey this is a test to see if it emails wav files."
attach = 'test.wav'

msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to
msg['Subject'] = subject
msg.attach(MIMEText(text))

part = MIMEBase('application', 'octect-stream')
part.set_payload(open(attach, 'rb').read())

Encoders.encode_base64(part)
part.add_header('Content-Dispostion', 'attachment; filename=%s"' % os.path.basename(attach))

msg.attach(part)
mailServer = smtplib.SMTP("smtp.gmail.com",587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(gmail_user, gmail_pwd)
mailServer.sendmail(gmail_user, to, msg.as_string())
mailServer.close()
print("Email Sent!")





