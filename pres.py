from flask import Flask # pythin web server for browser controls
from subprocess import Popen # runs command line programs
app = Flask(__name__) # creating actual web server


def pix(folder): # creating function to run eeach command line name
    
    Popen(["/bin/bash", "/home/pi/wwt-villa/slideshow.sh", "/home/pi/wwt-villa/" + folder]) # running the images
    return folder # returns text to display back in browser


@app.route("/<folder>") # defining browser route
def showpix(folder): # function "allClear" will run
    return pix(folder) # running alert function and returns alert message for "allClear"





app.run(host="0.0.0.0") # running the web server
