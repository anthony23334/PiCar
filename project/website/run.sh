#!/bin/bash
WEB_PORT=5000
CAM_PORT=8000
CLASS_IP=132.236.79.205
# Make sure that you kill any prev camera instances running! 
kill $(pgrep -f 'python3')

echo '====== Welcome to PiCar (Server) ======'
echo 'Please enter your netid: '
read netid 

if [[ $1 -eq 0 ]] ; then 
  # Open the camera tunnel (RECV):
  echo '====== Ssh-tunneling camera (9999) ====== '
  ssh -fNR 9999:localhost:$CAM_PORT $netid@$CLASS_IP > /dev/null
  echo "*********done*********"

  echo ""
  echo ""

  # Start the camera server and put in the background 
  echo '====== Starting the camera server (8000) ======'
  python3 ../camera/cam.py & > /dev/null
  echo '*********done*********'

  echo ""
  echo ""

  # Open the website tunnel(RECV):
  echo '====== Ssh-tunneling server (8888) ======'
  ssh -fNR 8888:localhost:$WEB_PORT $netid@$CLASS_IP > /dev/null 
  echo '*********done*********'

  echo ""
  echo ""
fi 
if [[ $1 -eq 1 ]] ; then 
  # Start the camera server and put in the background 
  echo '====== Starting the camera server (8000) ======'
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
