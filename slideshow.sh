#! /bin/bash
PHOTODIR=$1
INTERVAL=5
pkill -9 fbi
fbi -T 1 -d /dev/fb0 -noverbose -a -t $INTERVAL -u `find $PHOTODIR -iname "*.jpg" -o -iname "*.png"`
