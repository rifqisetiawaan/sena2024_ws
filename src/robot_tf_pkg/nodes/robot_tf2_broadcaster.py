#!/usr/bin/env python3
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg
from std_msgs.msg import Float32
from robot_tf_pkg.msg import encoder
import math
import numpy as np


def handle_turtle_pose(msg, turtlename):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    # konversi pulsa ke mm
    dist1 = 2*3.14*50*(msg.enc1/135)
    dist2 = 2*3.14*50*(msg.enc2/135)
    dist3 = 2*3.14*50*(msg.enc3/135)

    # kalkulasi encoder 3 roda
    vy = (dist1*(math.cos(30)))-(dist2*(math.cos(30)))
    vx = dist3-(dist1*(math.sin(30)))-(dist2*(math.sin(30)))
    vo = (dist1/215)+(dist2/215)+(dist3/215)

    # coord kartesian

    a = [[math.cos(vo), math.sin(-vo), 0], [math.sin(vo), math.cos(vo), 0], [0, 0, 1]]
    b = [vy, vx, vo]
    koor = np.dot(a,b)
    [xpos, ypos, theta] = koor

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "robot"
    t.transform.translation.x = xpos/1000
    t.transform.translation.y = ypos/1000
    # t.transform.translation.x = 0.7
    # t.transform.translation.y = 0.4
    t.transform.translation.z = 0
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, vo)
    # t.transform.rotation.x = q[0]
    # t.transform.rotation.y = q[1]
    # t.transform.rotation.z = q[2]
    # t.transform.rotation.w = q[3]
    t.transform.rotation.x = 0
    t.transform.rotation.y = 0
    t.transform.rotation.z = 0
    t.transform.rotation.w = 1

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