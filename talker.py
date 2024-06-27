#!/usr/bin/env python
# Software License Agreement (BSD License)
#

# Import the necessary libraries
import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

def talker():
    pub = rospy.Publisher('chatter', Image, queue_size=100)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    cap = cv2.VideoCapture(0)
    br = CvBridge()
    while not rospy.is_shutdown():
    	ret, frame = cap.read()
        
        # Print debugging information to the terminal
        rospy.loginfo('publishing video frame')
        cv2.imshow("camera", frame)
        cv2.waitKey(1)
        pub.publish(br.cv2_to_imgmsg(frame))
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
