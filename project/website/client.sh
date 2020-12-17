#!/bin/bash
WEB_PORT=5000
CAM_PORT=8000
CLASS_IP=132.236.79.205

WEB_PORT_CLASS=0
CAM_PORT_CLASS=0

# Make sure that you kill any prev camera instances running! 
kill $(pgrep -f 'python3') > /dev/null 

echo '====== Welcome to PiCar (Client) ======'
echo 'Please enter your netid: '
read netid 

if [[ "$netid" == "akk72" ]] ; then 
  WEB_PORT_CLASS=8888
  CAM_PORT_CLASS=9999
fi 

if [[ "$netid" == "an474" ]] ; then 
  WEB_PORT_CLASS=2222
  CAM_PORT_CLASS=3333
fi 

if [[ $1 -eq 0 ]] ; then 
  # Open the camera tunnel (RECV):
  echo '====== Ssh-tunneling camera ====== '
  ssh -fNL $CAM_PORT:localhost:$CAM_PORT_CLASS $netid@$CLASS_IP 
  echo "*********done*********"

  echo ""
  echo ""

  # Open the website tunnel(RECV):
  echo '====== Ssh-tunneling server ======'
  ssh -fNL $WEB_PORT:localhost:$WEB_PORT_CLASS $netid@$CLASS_IP 
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



