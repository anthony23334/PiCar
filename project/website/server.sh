#!/bin/bash

# File:        server.sh
# Date:        Dec. 17. 2020
# Author:      Anthony Ngoma (an474), Tsetse Kludze(akk72)
# The entry point for the server authenticating into PiCar and launching the server. 

WEB_PORT=5000
CAM_PORT=8000
CLASS_IP=132.236.79.205

WEB_PORT_CLASS=0
CAM_PORT_CLASS=0

# Make sure that you kill any prev camera instances running! 
kill $(pgrep -f 'python3')

echo '====== Welcome to PiCar (Server) ======'
echo 'Please enter your netid: '
read netid 

if [[ "$netid" == "an474" ]] ; then 
  WEB_PORT_CLASS=8888
  CAM_PORT_CLASS=9999
fi 

if [[ "$netid" == "akk72" ]] ; then 
  WEB_PORT_CLASS=2222
  CAM_PORT_CLASS=3333
fi 

if [[ $1 -eq 0 ]] ; then 
  # Open the camera tunnel (RECV):
  echo '====== Ssh-tunneling camera ====== '
  ssh -fNR $CAM_PORT_CLASS:localhost:$CAM_PORT $netid@$CLASS_IP > /dev/null
  echo "*********done*********"

  # Open the website tunnel(RECV):
  echo '====== Ssh-tunneling server ======'
  ssh -fNR $WEB_PORT_CLASS:localhost:$WEB_PORT $netid@$CLASS_IP > /dev/null 
  echo '*********done*********'

  echo ""
  echo ""
fi 

# Testing code 
if [[ $1 -eq 1 ]] ; then 
  # Start the camera server and put in the background 
  echo '====== Starting the camera server ======'
  #python3 ../camera/cam.py & > /dev/null
  echo '*********done*********'
fi 

echo '====== Welcome MASTER ======'

echo '====== Starting the website server ======'
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1

# start the server 
flask run --host=0.0.0.0 --port=$WEB_PORT 
