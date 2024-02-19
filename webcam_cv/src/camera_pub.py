#!/usr/bin/env python3

#this code publishes the video from the webcam to a topic

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

publisherNodeName='camera_sensor_publisher'
topic='/camera/rgb/image_raw'

rospy.init_node(publisherNodeName,anonymous=True)
publisher = rospy.Publisher(topic,Image,queue_size=60)

rate=rospy.Rate(30)

videoCaptureObject =cv2.VideoCapture(0)
bridgeObject=CvBridge()

while not rospy.is_shutdown():
    returnValue,capturedFrame = videoCaptureObject.read()
    if returnValue == True:
        rospy.loginfo('Video frame captured and published')
        imageToTransmit=bridgeObject.cv2_to_imgmsg(capturedFrame,'rgb8')
        publisher.publish(imageToTransmit)
    rate.sleep()