
import requests
import os
from pprint import pprint


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass

key = os.environ.get('NEWS_API')

url = f'https://newsapi.org/v2/everything?q=nasa\
        &from=2022-03-30\
        &sortBy=publishedAt\
        &apiKey={key}'

response = requests.get(url)
                       
content = response.text

pprint(content)



