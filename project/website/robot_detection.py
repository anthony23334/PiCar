"""
File:        robot_detection.py
Date:        Dec. 17. 2020
Author:      Anthony Ngoma (an474), Tsetse Kludze(akk72)
"""

import cv2
import numpy as np
import os
import io
import time
import picamera
from robot_control import RobotControl

class RobotDetection(object):
  """
  A class used to represent any robot movement that RPi can perform.
  """
  def __init__(self, rc):
    self.orb = cv2.ORB_create(nfeatures=3000)
    #Determines if the image was a good match
    #Kp stands for keypoints
    #dest
    self.desList = []
    self.images = []
    self.classNames = []
    self.turn_count = 0
    self.rc = rc


  def load_images(self, path_name):
    path = path_name
    myList = os.listdir(path)
    for cl in myList:
      imgCur = cv2.imread(f'{path}/{cl}', 0)
      self.images.append(imgCur)
      self.classNames.append(os.path.splitext(cl)[0])
    for img in self.images:
      kp,des = self.orb.detectAndCompute(img,None)
      self.desList.append(des)
  
  def findID(self, img, thres=100):
    if(len(self.desList) > 0 ):
      kp2,des2 = self.orb.detectAndCompute(img,None)

      bf = cv2.BFMatcher(cv2.NORM_HAMMING)
      matchList = []
      try:
        for des in self.desList:
          matches = bf.knnMatch(des,des2,k=2)
          good = []
          for m,n in matches:
            if m.distance < 0.75*n.distance:
              good.append([m])
          matchList.append(len(good))
      except:
        pass
      print(matchList)
      if(len(matchList) == 1):
          if max(matchList) > thres:
            return True, self.classNames[0]
          else:
            return False, 'Object Not Found'

      elif(len(matchList) > 1):
        if max(matchList) > thres:
            finalVal = matchList.index(max(matchList))
            return True, self.classNames[finalVal]
        else:
            return False, 'Object Not Found'

      elif(len(matchList)==0):
            return False, 'Object Not Found'
    else:
      return  False, 'No object was chosen to be identify'

  def start(self):
    self.load_images('Photos')
    count = 0
    Found = False
    # Create the in-memory stream
    straight_time = 3
    turn_time = 0.5
    with picamera.PiCamera() as camera:
      while True:
        count = 0
        while ((Found != True) and count < 5):
          stream = io.BytesIO()
          camera.start_preview()
          camera.capture(stream, format='jpeg')
          # Construct a numpy array from the stream
          data = np.fromstring(stream.getvalue(), dtype=np.uint8)
          # "Decode" the image from the array, preserving colour
          image = cv2.imdecode(data, 1)
          # OpenCV returns an array with data in BGR order. If you want RGB instead
          # use the following...
          img2 = image[:, :, ::-1]
          # success, img2 = self.cap.read()
          imgOriginal = img2.copy()
          img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
          Found, Name = self.findID(img2)
          if (Found == False):
            count = count + 1
        if(Found):
            print('object was found')
            print(Name)
            # cv2.VideoCapture.release(self.cap)
            # cv2.destroyAllWindows()
            break
        else:
            print('object location still in progress')
            straight_time = self.rc.automonous(straight_time, turn_time)
