#!/usr/bin/env python
# Software License Agreement (BSD License)


import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
import imutils
import numpy as np 

def callback(data):
 
  # Used to convert between ROS and OpenCV images
  br = CvBridge()
 
  # Output debugging information to the terminal
  rospy.loginfo("receiving video frame")
   
  # Convert ROS Image message to OpenCV image
  
  current_frame = br.imgmsg_to_cv2(data)
 
  # Display image
  
   
  
  #code to change the image
  pub = rospy.Publisher('changed', Image, queue_size=100)
  
  
  
  
  
    
  
  # Print debugging information to the terminal
  rospy.loginfo('changing video frame')
  hsv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
  lower_range = np.array([110,50,50])
  upper_range = np.array([130,255,255])
  mask = cv2.inRange(hsv, lower_range, upper_range)
  pub.publish(br.cv2_to_imgmsg(mask))
    
  

  
  

def changer():

  # Tells rospy the name of the node.
  # Anonymous = True makes sure the node has a unique name. Random
  # numbers are added to the end of the name. 
  rospy.init_node('img_changer', anonymous=True)
   
  # Node is subscribing to the video_frames topic
  rospy.Subscriber('chatter', Image, callback)




  
 
  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()
 
  # Close down the video stream when done
  cv2.destroyAllWindows()

if __name__ == '__main__':
    changer()
