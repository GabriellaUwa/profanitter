from TwitterSearch import *
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('config.properties')

class Tweets:

    search_order = TwitterSearchOrder()

    consumer_key = config["KEYS"]['consumer_key']
    consumer_secret = config["KEYS"]['consumer_secret']
    access_token = config["KEYS"]['access_token']
    access_token_secret = config["KEYS"]['access_token_secret']

    temp = []

    def __init__(self, *keywords):

        self.ts = TwitterSearch(
            consumer_key = self.consumer_key,
            consumer_secret = self.consumer_secret,
            access_token = self.access_token,
            access_token_secret = self.access_token_secret
         )

        self.search_order.set_keywords(keywords)
        self.search_order.set_language('eng')
        self.search_order.set_include_entities(False)

    def get_tweets(self):

        for tweet in self.ts.search_tweets_iterable(self.search_order):
            self.temp.append(tweet['text'])

        return self.temp #temporary just to see if I recieve tweets