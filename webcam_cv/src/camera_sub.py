#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

subscriberNodeName='camera_sensor_subscriber'
topic='/camera/rgb/image_raw'

def callbackFunction(message):
    bridgeObject=CvBridge()
    rospy.loginfo('received a video message/frame')
    covertedFrameBacktToCV=bridgeObject.imgmsg_to_cv2(message,'rgb8')

    cv2.imshow('camera',covertedFrameBacktToCV)

    cv2.waitKey(1)

rospy.init_node(subscriberNodeName,anonymous=True)
rospy.Subscriber(topic,Image,callbackFunction)
rospy.spin()
cv2.destroyAllWindows()