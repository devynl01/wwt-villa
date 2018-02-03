#! /bin/bash
PHOTODIR=$1 # here this is the passed photo directory for images we want to run
INTERVAL=5 #number of second to change the images
pkill -9 fbi #stops all fbi programs that are currently running
fbi -T 1 -d /dev/fb0 -noverbose -a -t $INTERVAL -u `find $PHOTODIR -iname "*.jpg" -o -iname "*.png"` # finding all the pictures and then putting them into fbi for slideshow
