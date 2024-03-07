from flask import Flask, render_template
import requests
import json

app = Flask(__name__)



def get_data():
    url = " https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response['preview'][-1]
    sub_reddit = response['subreddit']
    return meme_large, sub_reddit
    
@app.route('/')

def index():
    meme_large, sub_reddit = get_data()
    return render_template('index.html', meme=meme_large, sub_reddit=sub_reddit)

app.run(port=5000, debug=True)