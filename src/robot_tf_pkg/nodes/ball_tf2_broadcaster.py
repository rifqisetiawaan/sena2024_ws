#!/usr/bin/env python3
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
from std_msgs.msg import Float32
from robot_tf_pkg.msg import encoder
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped
import math
import numpy as np


def handle_ball_pose(msg, turtlename):
    Ballpub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    posBall = PoseStamped()
    if msg.position.x == 0 and msg.position.y == 0:
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "robot"
        t.child_frame_id = turtlename
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
        q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        Ballpub.publish(posBall)
    else:
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "robot"
        t.child_frame_id = turtlename
        # t.transform.translation.x = (msg.position.x +335)/1000
        # t.transform.translation.y = (msg.position.y +240)/1000
        t.transform.translation.x = (msg.position.x)/1000
        t.transform.translation.y = (msg.position.y)/1000
        t.transform.translation.z = 0.0
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
        q = tf_conversions.transformations.quaternion_from_euler(0, 0, theta)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        Ballpub.publish(posBall)
    br.sendTransform(t)

def handle_robot_pose(msg):
    enc = encoder()
    global enc1
    global enc2
    global enc3
    global xpos
    global ypos
    global theta
    enc1 = msg.enc1
    enc2 = msg.enc2
    enc3 = msg.enc3
    vy = (enc1*(math.cos(30)))-(enc2*(math.cos(30)))
    vx = enc3-(enc1*(math.sin(30)))-(enc2*(math.sin(30)))
    vo = (enc1/215)+(enc2/215)+(enc3/215)

    # coord kartesian

    a = [[math.cos(vo), math.sin(-vo), 0], [math.sin(vo), math.cos(vo), 0], [0, 0, 1]]
    b = [vy, vx, vo]
    koor = np.dot(a,b)
    [xpos, ypos, theta] = koor
    

if __name__ == '__main__':
    rospy.init_node('tf2_ball_broadcaster')
    turtlename = rospy.get_param('~balls')
    rospy.Subscriber('enco_value',
                     encoder,
                     handle_robot_pose)
    rospy.Subscriber('ballPos_topic',
                     Pose,
                     handle_ball_pose,
                     turtlename)
    
    # rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=10)
    rospy.spin()