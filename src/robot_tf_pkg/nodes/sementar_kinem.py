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
    dist1 = 2*3.14*5*(msg.enc1/135)
    dist2 = 2*3.14*5*(msg.enc2/135)
    dist3 = 2*3.14*5*(msg.enc3/135)

    
    # vo_deg = math.degrees(vo)
    a_sin = math.sin(math.radians(30))
    b_cos = math.cos(math.radians(30))

    # kalkulasi encoder 3 roda
    vx = int(dist3 - dist1 * a_sin - dist2 * a_sin)
    vy = int(dist1 * b_cos - dist2 * b_cos)
    vo = -(dist1+dist2+dist3)/218
    vo = math.radians(vo)
    # coord kartesian
    # a = np.array([[math.cos(vo), math.sin(-vo), 0],
    #             [math.sin(vo), math.cos(vo), 0],
    #             [0, 0, 1]])
    # b = np.array([vx, vy, 0])
    # koor = np.dot(a,b)
    # [ypos, xpos, theta] = koor

    a = np.array([[math.cos(vo), math.sin(vo), 0],
                [math.sin(-vo), math.cos(vo), 0],
                [0, 0, 1]])
    b = np.array([vx, vy, vo])
    koor = np.dot(a,b)
    [xpos, ypos, theta] = koor

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "robot"
    t.transform.translation.x = xpos/1000
    t.transform.translation.y = ypos/1000
    t.transform.translation.z = 0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, math.radians(theta), axes='sxyz')
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, vo)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    rob_pos.position.x = vx/1000
    rob_pos.position.y = vy/1000
    rob_pos.orientation.z = vo

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