#!/usr/bin/env python3

# cam sub program from cam_stream.py
# processing image here

# library
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from opencv_tools.msg import OmniBallInfo

class BallInfo(object):
    
    def __init__(self, pub):
        self._pub = pub

    # callback akan dipanggil, jika class BallInfo dipanggil
    def callback(self,data):
        br = CvBridge()
        frame1 = br.imgmsg_to_cv2(data)
        rospy.loginfo("RECEIVED !!")

        obi = OmniBallInfo()
        obi.radius = 1
        obi.angle = 1
        obi.pos_known = 1
        obi.x_pos = 1
        obi.y_pos = 1
        obi.distance = 1

        self._pub.publish(obi)
        cv2.imshow('frame_cam',frame1)
        cv2.waitKey(1)

def main():
    # node
    rospy.init_node('yolo_find', anonymous=False)
    # pub
    pub = rospy.Publisher('omni_ball_info', OmniBallInfo)
    info = BallInfo(pub)
    # subscribe
    rospy.Subscriber('video_topic', Image, info.callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()