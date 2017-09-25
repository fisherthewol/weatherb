from flask import Flask, render_template
import urllib
import json
from redre import redred
from random import randint

app = Flask(__name__)


def weatherconv(apidict):
    """Return nice string for give weather"""
    if "Rain" in apidict:
        return "rainy"
    elif "Clouds" in apidict:
        return "cloudy"
    elif "Snow" in apidict:
        return "snowing"
    elif "Drizzle" in apidict:
        return "drizzly"


@app.route('/')
def index():
    cities = ((London, uk), (Sheffield, uk), (Manchester, uk), (Brighton, uk))
    citychoice = cities[randint(0, len(cities))][0]
    with urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q={},uk&appid=BLANK".format(citychoice) as url:
        jn = json.loads(url.read().decode())
        weathercond = str(jn["weather"][0]["main"])
        weatherstat = weatherconv(weathercond)
    ggif = redred(weathercond)
    return render_template("pstb.html", city=str(cityurl).title(), weather=weatherstat, backgif=ggif)



@app.route('/<cityurl>')
def postcd(cityurl):
    with urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q={},uk&appid=BLANK".format(cityurl)) as url:
        jn = json.loads(url.read().decode())
        weathercond = str(jn["weather"][0]["main"])
        weatherstat = weatherconv(weathercond)
    ggif = redred(weathercond)
    return render_template("pstb.html", city=str(cityurl).title(), weather=weatherstat, backgif=ggif)
