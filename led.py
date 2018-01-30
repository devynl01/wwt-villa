import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

alerts = {"allClear": 3, "tornado": 5, "fire": 7, "intruder": 11}

if len(argv) < 2 or argv[1] not in alerts.keys() + ["on", "off"]:
    exit("You must provide an argument like: " + str(alerts.keys()))


for alertName in alerts.keys():
    GPIO.setup(alerts[alertName], GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    if alertName == argv[1] or argv[1] == "on":
       GPIO.output(alerts[alertName],True)
       print "Turn on " + str(alerts[alertName])
    else:
        GPIO.output(alerts[alertName],False)
        print "Turn off " + str(alerts[alertName])
