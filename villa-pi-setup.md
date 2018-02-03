sudo raspi-config
change password
change locale
setup ssh
change overscan

#add wwt-villa network
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
network={
  ssid="wwt-villa"
  psk="Magic123"
  id_str="project"
}

#install vim text editor
sudo apt-get install vim

#install fbi
sudo apt-get install fbi

#install python2
sudo apt-get install python
sudo apt-get install python-pip
sudo apt-get install python-RPi.GPIO
sudo pip install flask

#install git
sudo apt-get install git

#install nodejs
wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v.lts.sh | bash

#install /opt/nodejs/bin/tplight command list: https://www.npmjs.com/package/tplink-lightbulb
npm i -g tplink-lightbulb

