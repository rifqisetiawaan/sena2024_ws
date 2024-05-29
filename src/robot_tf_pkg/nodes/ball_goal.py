#!/usr/bin/env python3
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
from std_msgs.msg import Float32
from robot_tf_pkg.msg import encoder
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
import math
import time
import numpy as np


def handle_ball_pose(msg):
    Ballpub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    # Ballpub = rospy.Publisher('/move_base/goal', PoseStamped, queue_size=10)
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    posBall = PoseStamped()
    if msg.position.x == 0 and msg.position.y == 0:
        # t.header.stamp = rospy.Time.now()
        # t.header.frame_id = "robot"
        # t.child_frame_id = turtlename
        # t.transform.translation.x = 0.0
        # t.transform.translation.y = 0.0
        # t.transform.translation.z = 0.0
        # # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        # t.transform.rotation.x = q[0]
        # t.transform.rotation.y = q[1]
        # t.transform.rotation.z = q[2]
        # t.transform.rotation.w = q[3]
        posBall.header.frame_id = 'map'
        posBall.header.stamp = rospy.Time.now()
        posBall.pose.position.x = 0.0
        posBall.pose.position.y = 0.0
        posBall.pose.position.z = 0.0
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        posBall.pose.orientation.x = 0
        posBall.pose.orientation.y = 0
        posBall.pose.orientation.z = 0
        posBall.pose.orientation.w = 1
    else:
        # t.header.stamp = rospy.Time.now()
        # t.header.frame_id = "robot"
        # t.child_frame_id = turtlename
        # t.transform.translation.x = (msg.position.x +335)/1000
        # t.transform.translation.y = (msg.position.y +240)/1000
        # t.transform.translation.z = 0.0
        # # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        # t.transform.rotation.x = q[0]
        # t.transform.rotation.y = q[1]
        # t.transform.rotation.z = q[2]
        # t.transform.rotation.w = q[3]
        posBall.header.frame_id = 'map'
        posBall.header.stamp = rospy.Time.now()
        # posBall.pose.position.x = (msg.position.x)/1000
        # posBall.pose.position.y = (msg.position.y)/1000
        posBall.pose.position.x = msg.position.x/1000
        posBall.pose.position.y = msg.position.y/1000
        posBall.pose.position.z = 0.0
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        posBall.pose.orientation.x = 0
        posBall.pose.orientation.y = 0
        posBall.pose.orientation.z = 0
        posBall.pose.orientation.w = 1
        # posBall.pose.orientation.x = q[0]
        # posBall.pose.orientation.y = q[1]
        # posBall.pose.orientation.z = q[2]
        # posBall.pose.orientation.w = q[3]

    Ballpub.publish(posBall)
    # time.sleep(5)
    # br.sendTransform(t)
    



if __name__ == '__main__':
    rospy.init_node('ball_goal')
    # turtlename = rospy.get_param('~balls')
    rospy.Subscriber('ballPos_topic',
                     Pose,
                     handle_ball_pose)
    
    # rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=10)
    rospy.spin()