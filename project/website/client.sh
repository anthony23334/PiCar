#!/bin/bash
WEB_PORT=5000
CAM_PORT=8000
CLASS_IP=132.236.79.205
# Make sure that you kill any prev camera instances running! 
kill $(pgrep -f 'python3') > /dev/null 

echo '====== Welcome to PiCar (Client) ======'
echo 'Please enter your netid:'
read netid 

if [[ $1 -eq 0 ]] ; then 
  # Open the camera tunnel (RECV):
  echo '====== Ssh-tunneling camera (9999) ====== '
  ssh -fNL $CAM_PORT:localhost:9999 $netid@$CLASS_IP 
  echo "*********done*********"

  echo ""
  echo ""

  # Open the website tunnel(RECV):
  echo '====== Ssh-tunneling server (8888) ======'
  ssh -fNL $WEB_PORT:localhost:8888 $netid@$CLASS_IP 
  echo '*********done*********'

  echo ""
  echo ""
fi 


# Welcome message
echo '====== Welcome to PiCar Website ======'
echo 'Client netid: '
echo $netid
echo 

echo 'Open VNCView and navigate to:'
printf 'http://localhost:5000'
echo 



