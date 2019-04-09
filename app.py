from flask import Flask, request
import re
from tweets import Tweets

app = Flask(__name__)

@app.route('/search', method=['GET', 'POST'])
def search():

    keyword = request.form['keyword']
    wordList = re.sub("[^\w]", " ", keyword).split()  # will strip punctuations later
    tw = Tweets(wordList)

    tw.get_tweets()

if __name__ == '__main__':
    app.run()
