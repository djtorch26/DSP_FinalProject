# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:29:36 2020
This works with python Version 3 only

@author: Dawson
"""

import os
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


gmail_user = "dtemail098@gmail.com"
gmail_pwd = "gmailAccount1"
to = "djtorch123@gmail.com"

def emailFile(file):
    
    attach = file 
    
    if "test" in file:
        subject = "Wave File"
        text = "This is the recorded voice from the Microphone.\n   To use this file you Must add the extension .wav to the no name file."
    if "voice" in file:
        subject = "PNG File"
        text = "This is a PNG file of the recorded voice.\n Add the .png once downloaded to view"
    
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
        
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    
    encoders.encode_base64(part)
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

#emailFile('test.wav')
#emailFile('voiceWave.png')
