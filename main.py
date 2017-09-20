from flask import Flask, render_template, request, redirect, url_for
import urllib
import json
import praw

app = Flask(__name__)
global start
start = True


def redred(strvar):
    reddit = praw.Reddit("wimgbot", 
                         user_agent="wthrbot:v100:t3rr0r_f3rr3t")
    subit = reddit.subreddit(


def weatherconv(apidict):
    if "Rain" in apidict:
        return "rainy."
    elif "Clouds" in apidict:
        return "cloudy."


@app.route('/')
def index():
    global start
    if start:
        return render_template("index.html")
    else:
        return redirect(url_for())


@app.route('/city/')
def postcd():
    cityurl = request.args.get("city")
    with urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q={},uk&appid=BLANK".format(cityurl)) as url:
        jn = json.loads(url.read().decode())
        weatherstat = weatherconv(str(jn["weather"][0]["main"]))
        return render_template("pstb.html", city=str(cityurl).title(), weather=weatherstat)
