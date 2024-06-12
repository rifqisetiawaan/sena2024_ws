#!/usr/bin/env python3
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg
from std_msgs.msg import Float32
from geometry_msgs.msg import Pose
from robot_tf_pkg.msg import encoder
import math
import numpy as np


def handle_turtle_pose(msg, turtlename):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    Robotpub = rospy.Publisher('robot_pos', Pose, queue_size=10)
    rob_pos = Pose()
    # konversi pulsa ke mm
    # dist1 = 2*3.14*50*(msg.enc1/130)
    # dist2 = 2*3.14*50*(msg.enc2/139)
    # dist3 = 2*3.14*50*(msg.enc3/133)
    dist1 = 2*3.14*5*(msg.enc1/135)
    dist2 = 2*3.14*5*(msg.enc2/135)
    dist3 = 2*3.14*5*(msg.enc3/137)
    # dist1 = msg.enc1*2.325
    # dist2 = msg.enc2*2.325
    # dist3 = msg.enc3*2.325

    # kalkulasi encoder 3 roda
    vx = dist1*(math.cos(30))-dist2*(math.cos(30))
    vy = dist3-dist1*(math.sin(30))-dist2*(math.sin(30))
    vo = (dist1/218)+(dist2/218)+(dist3/218)
    # ax = dist1*math.cos(30)
    # ay = dist1*math.sin(30)
    # bx = dist2*math.cos(150)
    # by = dist2*math.sin(150)
    # cx = dist3*math.cos(270)
    # cy = dist3*math.sin(270)

    # coord kartesian

    # a = [[math.cos(vo), math.sin(-vo), 0], [math.sin(vo), math.cos(vo), 0], [0, 0, 1]]
    a = np.array([[math.cos(vo), math.sin(-vo), 0],
                [math.sin(vo), math.cos(vo), 0],
                [0, 0, 1]])
    b = np.array([vx, vy, vo])
    koor = np.dot(a,b)
    # xpos = ax+bx+cx
    # ypos = ay+by+cy
    [ypos, xpos, theta] = koor
    # rospy.loginfo(xpos)

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "robot"
    t.transform.translation.x = (xpos/1000)
    t.transform.translation.y = (ypos/1000)
    t.transform.translation.z = 0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, theta, axes='sxyz')
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, vo)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]
    # t.transform.rotation.x = 0
    # t.transform.rotation.y = 0
    # t.transform.rotation.z = 0
    # t.transform.rotation.w = 1

    rob_pos.position.x = (xpos/1000)
    rob_pos.position.y = (ypos/1000)
    rob_pos.orientation.z = (theta/1000)

    Robotpub.publish(rob_pos)
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_robot_broadcaster')
    turtlename = rospy.get_param('~robot')
    rospy.Subscriber('enco_value',
                     encoder,
                     handle_turtle_pose,
                     turtlename)
    # rospy.Publisher()
    rospy.spin()