#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from robot_tf_pkg.msg import encoder
import math
import numpy as np


def feedback(msg):
    motPub = rospy.Publisher('/motor_value', encoder, queue_size=10)
    kinem = Twist()
    mot_val = encoder()
    x = msg.linear.x
    y = msg.linear.y
    z = 0

    matriks = np.array([[-0.33, 0.58, 0.33],
            [-0.33, -0.58, 0.33],
            [0.67, 0, 0.33]])
    pergerakan = np.array([x, y, z])
    # rospy.loginfo(x)

    hasil = np.dot(matriks, pergerakan)
    # hasil = np.dot(pergerakan, matriks)
 
    [mot1, mot2, mot3] = hasil

    mot_val.enc1 = mot1*255
    mot_val.enc2 = mot2*255
    mot_val.enc3 = mot3*255
    motPub.publish(mot_val)

    

if __name__ == '__main__':
    rospy.init_node('motor_process')
    # turtlename = rospy.get_param('~robot')
    rospy.Subscriber('/cmd_vel',Twist,feedback)
    rospy.spin()