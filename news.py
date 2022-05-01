import requests
import os
import datetime
from pprint import pprint


class NewsFeed:
    """Representing multiple news title and links as a single string
    """
    base_url = 'https://newsapi.org/v2/everything'
    api_key = os.environ.get('NEWS_API')
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    day_before = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    def __init__(self, interest, from_date=today, to_date=day_before):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date

    def get(self):
        url = f'{self.base_url}?' \
              f'q={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'sortBy=popularity&' \
              f'apiKey={self.api_key}'


        response = requests.get(url)
        content = response.json()

        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + '\n\t' + article['url'] + '\n\n'

        return email_body


if __name__ == '__main__':
    news_feed = NewsFeed(interest='Tiesto')
    print(news_feed.get())

