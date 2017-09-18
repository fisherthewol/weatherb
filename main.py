from flask import Flask, render_template, request
import urllib
import json
app = Flask(__name__)


def weatherconv(apidict):
    if "Rain" in apidict:
        return "rainy."
    elif "Clouds" in apidict:
        return "cloudy."


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<cityurl>')
def postcd(cityurl):
    with urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q={},uk&appid=BLANK".format(cityurl)) as url:
        jn = json.loads(url.read().decode())
        weatherstat = weatherconv(str(jn["weather"][0]["main"]))
        return render_template("pstb.html", city=str(cityurl).title(), weather=weatherstat)
