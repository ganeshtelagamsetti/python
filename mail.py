from subprocess import call
import time
import os
import glob
import smtplib,getpass
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

try:
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    password='abc'
    n=input('Enter valid task password:')
    if n==password:
        print("Succesful")
    else:
        print("Not valid Task Password")
        print("Now login your mail account")
        user=input('Enter your email:')
        pwd=getpass.getpass(prompt="Enter password:")
        server.login(user,pwd)
        print("Successfully loged in")
        to_mail=input("Enter mail ID to recieve alert:")
        alert_msg='This is just alert using python'
        server.sendmail(user,to_mail,alert_msg)
        print("Alert Mail sent")
except:
    print("Failed to send mail")
