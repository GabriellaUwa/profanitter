from flask import Flask, request
import re
from tweets import Tweets
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def search():

    keyword = request.form['keyword']
    wordList = re.sub("[^\w]", " ", keyword).split()  # will strip punctuations later
    tw = Tweets()

    for i in wordList:
        tw.clean(i)

    #return to the template

    return render_template("index.html")

@app.route('/')
def results():

    return render_template("results.html")

if __name__ == '__main__':
    app.run()
