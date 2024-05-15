#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Pose
from robot_tf_pkg.msg import encoder
import math
import numpy as np

def callback(msg):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.enc1)
    a = msg.enc1
    vy = (msg.enc1*(math.cos(30)))-(msg.enc2*(math.cos(30)))
    vx = msg.enc3-(msg.enc1*(math.sin(30)))-(msg.enc2*(math.sin(30)))
    vo = (msg.enc1/215)+(msg.enc2/215)+(msg.enc3/215)

    # coord kartesian

    a = [[math.cos(vo), math.sin(-vo), 0], [math.sin(vo), math.cos(vo), 0], [0, 0, 1]]
    b = [vy, vx, vo]
    koor = np.dot(a,b)
    [xpos, ypos, theta] = koor
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('odom', anonymous=True)

    rospy.Subscriber('enco_value', encoder, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass