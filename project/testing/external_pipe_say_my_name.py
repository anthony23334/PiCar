# mixed_input_pipe_say_my_name.py
import subprocess
import sys

proc = subprocess.Popen(["python", "robot_test.py"], stdin=subprocess.PIPE)

try:
  while proc.returncode is None:
    i = sys.stdin.read(1)
    if i == '':
        proc.stdin.close()
        break
    proc.stdin.write(i)
    proc.poll()

  while proc.returncode is None:
    proc.poll()
        

except KeyboardInterrupt:
  proc.stdin.write('exit')


