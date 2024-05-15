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

    # kalkulasi encoder 3 roda

    vy = (msg.enc1*(math.cos(30)))-(msg.enc2*(math.cos(30)))
    vx = msg.enc3-(msg.enc1*(math.sin(30)))-(msg.enc2*(math.sin(30)))
    vo = (msg.enc1/215)+(msg.enc2/215)+(msg.enc3/215)

    # coord kartesian

    a = [[math.cos(vo), math.sin(-vo), 0], [math.sin(vo), math.cos(vo), 0], [0, 0, 1]]
    b = [vy, vx, vo]
    koor = np.dot(a,b)
    [xpos, ypos, theta] = koor

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = turtlename
    t.transform.translation.x = xpos
    t.transform.translation.y = ypos
    t.transform.translation.z = 0
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

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