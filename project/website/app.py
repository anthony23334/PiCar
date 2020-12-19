"""
File:        app.py
Date:        Dec. 17. 2020
Author:      Anthony Ngoma (an474), Tsetse Kludze(akk72)
"""

from flask import Flask
from flask import render_template
from flask import request
import subprocess
import sys
from robot_control import RobotControl 
from werkzeug import secure_filename
import os 
from robot_detection import RobotDetection 
import time 

cam = 0
cam_proc= 0

rc = RobotControl()
rd = RobotDetection(rc)

app = Flask(__name__)

# Create a directory in a known location to save files to.
uploads_dir = 'Photos'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/control')
def control():
    global cam 
    global cam_proc
    if (cam == 0): 
        cam_proc = subprocess.Popen("exec python3 ../camera/cam.py > /dev/null", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        time.sleep( 1 ) # give time to create the process 
    cam = 1
    return render_template('control.html')

@app.route('/auto')
def auto():
    global cam
    global cam_proc
    # kill the process running camera: python3  
    if (cam == 1): 
        print(str(cam_proc.pid))
        cam_proc.kill()  

    cam = 0 
    return render_template('auto.html') 



@app.route('/robot_front', methods=['GET', 'POST'])
def robot_front():
    rc.go_straight(1)
    print("FRONT")  
    return ('', 204)

@app.route('/robot_back', methods=['GET', 'POST'])
def robot_back():
    rc.go_back(1)
    print("BACK")  
    return ('', 204)

@app.route('/robot_right', methods=['GET', 'POST'])
def robot_right():
    rc.turn_right(0.5)
    print("RIGHT")  
    return ('', 204)

@app.route('/robot_left', methods=['GET', 'POST'])
def robot_left():
    rc.turn_left(0.5);    
    print("LEFT")  
    return ('', 204)

@app.route('/robot_stop', methods=['GET', 'POST'])
def robot_stop():
    rc.stop();    
    print("STOP")  
    return ('', 204)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(uploads_dir, secure_filename("TEST.png")))
        rd.start()
        return 'FOUND THE TARGET'
