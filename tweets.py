import twitter
import configparser
from profanity_check import predict, predict_prob
from functools import reduce
import re

config = configparser.ConfigParser()
config.sections()
config.read('config.properties')

class Tweets:

    consumer_key = config["KEYS"]['consumer_key'].strip("\'")
    consumer_secret = config["KEYS"]['consumer_secret'].strip("\'")
    access_token = config["KEYS"]['access_token'].strip("\'")
    access_token_secret = config["KEYS"]['access_token_secret'].strip("\'")

    cleaned = []
    details = {}

    def __init__(self):

        self.api = twitter.Api(consumer_key=self.consumer_key,
                               consumer_secret=self.consumer_secret,
                               access_token_key=self.access_token,
                               access_token_secret=self.access_token_secret)

    def get_tweets(self, word):

        statuses = self.api.GetSearch(term=word,
                                      count=100,
                                      lang='en',
                                      since="2018-01-01",
                                      return_json=True)['statuses']
        return [i['text'] for i in statuses]

    def clean(self, word):
        for i in self.get_tweets(word):
            self.strip_out(i)
        self.add_to_dict(word)


    def strip_out(self, text):

        text = re.sub(r"http\S+", "", text)
        text = re.sub(r'[^\w]', ' ', text).strip()
        self.cleaned.append(text.strip())

    def add_to_dict(self, word):
        self.details[word] = self.cleaned
        self.cleaned = []
"""
dummy tests
t = Tweets()
print(t.get_tweets())
t.clean()

p = predict_prob(t.cleaned)

print(t.cleaned)
print(reduce(lambda x, y: x*y, p.tolist()))
print(p.tolist())
"""