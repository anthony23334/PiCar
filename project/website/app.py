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

# proc = subprocess.Popen(["python", "../testing/robot_test.py"], stdin=subprocess.PIPE)

rc = RobotControl()
rd = RobotDetection(rc)

app = Flask(__name__)

# Create a directory in a known location to save files to.
uploads_dir = 'Photos'

@app.route('')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/auto')
def auto():
    return render_template('auto.html') 


@app.route('/robot_front', methods=['GET', 'POST'])
def robot_front():
    # global proc 
    # proc.stdin.write(str.encode('f'))
    rc.go_straight(1)
    print("FRONT")  
    return ('', 204)

@app.route('/robot_back', methods=['GET', 'POST'])
def robot_back():
    # global proc 
    # proc.stdin.write(str.encode('b'))
    rc.go_back(1)
    print("BACK")  
    return ('', 204)

@app.route('/robot_right', methods=['GET', 'POST'])
def robot_right():
    # proc.stdin.write('r')
    rc.turn_right(0.5)
    print("RIGHT")  
    return ('', 204)

@app.route('/robot_left', methods=['GET', 'POST'])
def robot_left():
    # proc.stdin.write('l')
    rc.turn_left(0.5);    
    print("LEFT")  
    return ('', 204)

@app.route('/robot_stop', methods=['GET', 'POST'])
def robot_stop():
    # proc.stdin.write('l')
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
