from flask import Flask
from subprocess import Popen
app = Flask(__name__)

alerts = {"allClear": {"message": "All Clear"}, "fire": {"message": "Fire"}, "tornado": {"message": "Tornado"}, "intruder": {"message": "Intruder"}}


def alert(alertName):
    Popen(["/usr/bin/python", "/home/pi/led.py", alertName])
    
    Popen(["/home/pi/slideshow.sh", alertName])
    return alerts[alertName]["message"]


@app.route("/all-clear")
def allClear():
    return alert("allClear")


@app.route("/fire")
def fire():
    return alert("fire")


@app.route("/tornado")
def tornado():
    return alert("tornado")


@app.route("/intruder")
def intruder():
    return alert("intruder")


app.run(host="0.0.0.0")
