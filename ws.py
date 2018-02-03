from flask import Flask # pythin web server for browser controls
from subprocess import Popen # runs command line programs
app = Flask(__name__) # creating actual web server

alerts = {"allClear": {"message": "All Clear", "hex": "#ffffff"}, "fire": {"message": "Fire", "hex": "#E32A3C"}, "tornado": {"message": "Tornado", "hex": "#00ff00"}, "intruder": {"message": "Intruder", "hex": "#8682EE"}} # named list with the browser message and hex color code
Popen(["/opt/nodejs/bin/tplight", "on", "192.168.62.137"]) # turning the wireless light on

def alert(alertName): # creating function to run eeach command line name
    Popen(["/usr/bin/python", "/home/pi/wwt-villa/led.py", alertName]) # running GPIO led lights
    Popen(["/opt/nodejs/bin/tplight", "hex", "192.168.62.137", alerts[alertName]["hex"]]) # running wireless light 
    Popen(["/bin/bash", "/home/pi/wwt-villa/slideshow.sh", "/home/pi/wwt-villa/" + alertName]) # running the images
    return alerts[alertName]["message"] # returns text to display back in browser


@app.route("/all-clear") # defining browser route
def allClear(): # function "allClear" will run
    return alert("allClear") # running alert function and returns alert message for "allClear"


@app.route("/fire") # defining browser route
def fire(): # function "fire" will run
    return alert("fire") # running alert function and returns alert message for " Fire"


@app.route("/tornado") # defining browser route
def tornado(): # function "tornado " will run
    return alert("tornado") # running alert function and returns alert message "tornado"


@app.route("/intruder") # defines browser route	
def intruder(): # function "intruder" will run
    return alert("intruder") # running alert function and returns alert message "intruder"


app.run(host="0.0.0.0") # running the web server
