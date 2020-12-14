import time
import RPi.GPIO as GPIO
import sys 

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...

GPIO.setup(5, GPIO.OUT)
pa = GPIO.PWM(5, 50)
GPIO.setup(20, GPIO.OUT)
pb = GPIO.PWM(20, 50)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)


ai1 = 6 
ai2 = 26 
bi1 = 12 
bi2 = 16 
GPIO.setup(ai1, GPIO.OUT)
GPIO.setup(ai2, GPIO.OUT)
GPIO.setup(bi1, GPIO.OUT)
GPIO.setup(bi2, GPIO.OUT)
turn = 0; 


# turns: 0 -> stop, 1 -> CW, 2 -> CCW
def run(serv_leter, turn):
    if ( serv_leter == 'a'):
        if (turn == 0):
            GPIO.output( ai1, GPIO.HIGH)
            GPIO.output( ai2, GPIO.HIGH)
        elif (turn == 1):
            GPIO.output( ai1, GPIO.HIGH)
            GPIO.output( ai2, GPIO.LOW)
        elif (turn == 2):
            GPIO.output( ai2, GPIO.HIGH)
            GPIO.output( ai1, GPIO.LOW)
    else:
        if (turn == 0):
            GPIO.output( bi1, GPIO.HIGH)
            GPIO.output( bi2, GPIO.HIGH)
        elif (turn == 1):
            GPIO.output( bi1, GPIO.HIGH)
            GPIO.output( bi2, GPIO.LOW)
        elif (turn == 2):
            GPIO.output( bi2, GPIO.HIGH)
            GPIO.output( bi1, GPIO.LOW)

pa.start(50)
pb.start(50)

print "PASS INPUTTT..."
for direction in iter(sys.stdin.readline, ''):
  direction = direction[:-1]
  print "what's your direction?{0}?".format(direction)
  if direction == "exit":
    run("a", 0)
    run("b", 0)
    break
  if direction == "f":
    print ("FORWARD")
    # back
    run("a", 2)
    run("b", 2)
  elif direction == "b":
    print ("BACK")
    # back
    run("a", 1)
    run("b", 1)
  elif direction == "s":
    print ("STOP")
    # back
    run("a", 0)
    run("b", 0)
  elif direction == "l":
    print ("LEFT")
    # back
    run("a", 2)
    run("b", 0)
  elif direction == "r":
    print ("RIGHT")
    # back
    run("a", 0)
    run("b", 2)

pa.stop()
pb.stop()
GPIO.cleanup()