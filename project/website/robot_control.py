import RPi.GPIO as GPIO
import time

class RobotControl(object):
    def __init__(self):
        self.ai1 = 6 
        self.ai2 = 26 
        self.bi1 = 12 
        self.bi2 = 16 
        GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
        GPIO.setwarnings(False)
        GPIO.setup(5, GPIO.OUT)
        self.pa = GPIO.PWM(5, 50)
        GPIO.setup(20, GPIO.OUT)
        self.pb = GPIO.PWM(20, 50)
        GPIO.setup(self.ai1, GPIO.OUT)
        GPIO.setup(self.ai2, GPIO.OUT)
        GPIO.setup(self.bi1, GPIO.OUT)
        GPIO.setup(self.bi2, GPIO.OUT)
        self.pa.start(60)
        self.pb.start(60)
        self.movement_counter = 0
        
    # turns: 0 -> stop, 1 -> CW, 2 -> CCW
    def run(self, serv_leter, turn):
        if ( serv_leter == 'a'):
            if (turn == 0):
                GPIO.output( self.ai1, GPIO.HIGH)
                GPIO.output( self.ai2, GPIO.HIGH)
            elif (turn == 1):
                GPIO.output( self.ai1, GPIO.HIGH)
                GPIO.output( self.ai2, GPIO.LOW)
            elif (turn == 2):
                GPIO.output( self.ai2, GPIO.HIGH)
                GPIO.output( self.ai1, GPIO.LOW)
        else:
            if (turn == 0):
                GPIO.output( self.bi1, GPIO.HIGH)
                GPIO.output( self.bi2, GPIO.HIGH)
            elif (turn == 1):
                GPIO.output( self.bi1, GPIO.HIGH)
                GPIO.output( self.bi2, GPIO.LOW)
            elif (turn == 2):
                GPIO.output( self.bi2, GPIO.HIGH)
                GPIO.output( self.bi1, GPIO.LOW)
      
    def front(self):
        print("Forward...")
        self.run("a", 2)
        self.run("b", 2)

    def back(self):
        print("Backward...")
        self.run("a", 1)
        self.run("b", 1)
    
    def right(self):
        print("Right...")
        self.run("a", 2)
        self.run("b", 0)

    def left(self):
        print("Left...")
        self.run("a", 0)
        self.run("b", 2)

    def stop(self):
        print("Stop...")
        self.run("a", 0)
        self.run("b", 0)

    def turn_right(self, turn_time):
        self.right()
        Time_diff = 0
        start_time = time.time()
        while(Time_diff < turn_time):
            Now = time.time() 
            Time_diff = Now - start_time 
        self.stop()

    def turn_left(self, turn_time):
        self.left()
        Time_diff = 0
        start_time = time.time()
        while(Time_diff < turn_time):
            Now = time.time() 
            Time_diff = Now - start_time 
        self.stop()
    
    def go_straight(self, straight_time):
        self.front()
        Time_diff = 0
        start_time = time.time()
        while(Time_diff < straight_time):
            Now = time.time() 
            Time_diff = Now - start_time 
        self.stop()
        
    def go_back(self, back_time):
        self.back()
        Time_diff = 0
        start_time = time.time()
        while(Time_diff < back_time):
            Now = time.time() 
            Time_diff = Now - start_time 
        self.stop()

    def automonous(self, straight_time, turn_time):
        if(straight_time != 0):
            if (self.movement_counter % 2 == 0):
                self.go_straight(straight_time)
                self.movement_counter =self.movement_counter +1
                return straight_time - .5
            elif (self.movement_counter % 2 == 1):
                self.turn_right(turn_time)
                self.movement_counter =self.movement_counter +1
        return straight_time 

        
#rc = RobotControl(3, 0.5)
#rc.automonous()





