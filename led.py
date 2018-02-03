from sys import argv # command line arguments
import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setwarnings(False) # we don't want to see warnings 
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering for rpi

alerts = {"allClear": 3, "tornado": 5, "fire": 7, "intruder": 11} # named list for our alerts relating to GPIO ports

if len(argv) < 2 or argv[1] not in alerts.keys() + ["on", "off"]: # argument checking
    exit("You must provide an argument like: " + str(alerts.keys())) # stop if you didn't give us a valid argument


for alertName in alerts.keys(): # loop through the possible alertNames
    GPIO.setup(alerts[alertName], GPIO.OUT) ## Setup all used GPIO Pins to OUT
    if alertName == argv[1] or argv[1] == "on": # if command line is one it is true if matched, if not matched: false
       GPIO.output(alerts[alertName],True) #turns on led light
       print "Turn on " + str(alerts[alertName]) # tells which GPIO port we turned on
    else:
        GPIO.output(alerts[alertName],False) # if it doesn't match it's false and turn off that GPIO port
        print "Turn off " + str(alerts[alertName]) #Which GPIO port is turned off
