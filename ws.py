from flask import Flask
from subprocess import Popen
app = Flask(__name__)

alerts = {"allClear": {"message": "All Clear", "hex": "#ffffff"}, "fire": {"message": "Fire", "hex": "#E32A3C"}, "tornado": {"message": "Tornado", "hex": "#56E32A"}, "intruder": {"message": "Intruder", "hex": "#8682EE"}}
Popen(["/opt/nodejs/bin/tplight", "on", "192.168.62.137"])

def alert(alertName):
    Popen(["/usr/bin/python", "/home/pi/wwt-villa/led.py", alertName])
    Popen(["/opt/nodejs/bin/tplight", "hex", "192.168.62.137", alerts[alertName]["hex"]])   
    Popen(["/bin/bash", "/home/pi/wwt-villa/slideshow.sh", "/home/pi/wwt-villa/" + alertName])
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
