from email.mime.text import MIMEText
import smtplib
import os
from os.path import join, dirname
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# SMTP認証情報
account = os.environ.get("MAIL_USERNAME")
password = os.environ.get("MAIL_PASSWORD")
# 送信元
from_email = os.environ.get("MAIL_USERNAME")
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.environ.get("ServiceAccountCredentials"), scope)
client = gspread.authorize(creds)

sheet = client.open("connect_mail").sheet1

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

for target in list_of_hashes:
    msg = MIMEText(target['contents'], "html")
    msg["Subject"] = target['subject']
    msg["To"] = target['email']
    msg["From"] = from_email

    # メール送信処理
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(account, password)
    server.send_message(msg)
    server.quit()
