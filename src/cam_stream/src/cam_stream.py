#!/usr/bin/env python3

# cam stream program, pub ke yolo_dist
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def publish_message():
    pub = rospy.Publisher('video_topic', Image, queue_size=10)
    rospy.init_node('webcam_stream', anonymous=False)

    rate = rospy.Rate(10)

    cap = cv2.VideoCapture(0)
    br = CvBridge()
    

    while not rospy.is_shutdown():
        # capture frame by frame
        ret, frame = cap.read()

        if ret==True:
            rospy.loginfo('publishing video frame')

            # publish and convert img to ros format
            pub.publish(br.cv2_to_imgmsg(frame))

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_message()
    except rospy.ROSInterruptException:
        pass