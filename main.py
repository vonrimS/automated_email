import time

import yagmail
import os
import pandas
import datetime
from news import NewsFeed

mail_addr = os.environ.get('automated_mail_addr')
mail_pass = os.environ.get('automated_mail_pass')


def send_email():
    news_feed = NewsFeed(interest=row['interest'])
    email = yagmail.SMTP(user=mail_addr, password=mail_pass)
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}!\n\n See what's on about {row['interest']} today.\n\n {news_feed.get()}\n\nHave a nice day! ")


while True:
    if datetime.datetime.now().hour == 21 and datetime.datetime.now().minute == 15:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)


