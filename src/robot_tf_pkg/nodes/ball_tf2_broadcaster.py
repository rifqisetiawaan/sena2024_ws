#!/usr/bin/env python3
import rospy

# Because of transformations
import tf2_ros
import geometry_msgs.msg
from std_msgs.msg import Float32
from robot_tf_pkg.msg import encoder
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped
import math
import numpy as np

def handle_robot_pose(msg):
    global xpos
    global ypos
    xpos = msg.position.x
    ypos = msg.position.y
    
def handle_ball_pose(msg, turtlename):
    global xpos
    global ypos
    Ballpub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    # Ballpub = rospy.Publisher('/move_base/current_goal', PoseStamped, queue_size=10)
    # Ballpub = rospy.Publisher('/goal', PoseStamped, queue_size=10)
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    posBall = PoseStamped()
    X = xpos/1000 + ((msg.position.x-320)/1000)*2
    Y = ypos/1000 + ((msg.position.y-210)/1000)*2
    # X = 0.5
    # Y = 1.5

    # x_new = X * math.cos(math.radians(135)) - Y * math.sin(math.radians(135))
    # y_new = X * math.cos(math.radians(135)) + Y * math.sin(math.radians(135))
    if msg.position.x == 0 and msg.position.y == 0:
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "map"
        t.child_frame_id = turtlename
        t.transform.translation.x = xpos/1000
        t.transform.translation.y = ypos/1000
        t.transform.translation.z = 0.0
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        t.transform.rotation.x = 0
        t.transform.rotation.y = 0
        t.transform.rotation.z = 0.71
        t.transform.rotation.w = 0.71
        # ------------
        posBall.header.frame_id = 'map'
        posBall.header.stamp = rospy.Time.now()
        posBall.pose.position.x = xpos/1000
        posBall.pose.position.y = ypos/1000
        posBall.pose.position.z = 0.0
        posBall.pose.orientation.x = 0
        posBall.pose.orientation.y = 0
        posBall.pose.orientation.z = 0.71
        posBall.pose.orientation.w = 0.71
        Ballpub.publish(posBall)
    else:
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "map"
        t.child_frame_id = turtlename
        # t.transform.translation.x = (msg.position.x +335)/1000
        # t.transform.translation.y = (msg.position.y +240)/1000
        t.transform.translation.x = X
        t.transform.translation.y = Y
        # posBall.pose.position.x = 0.3
        # posBall.pose.position.y = 1.8
        t.transform.translation.z = 0.0
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        # t.transform.rotation.x = q[0]
        # t.transform.rotation.y = q[1]
        # t.transform.rotation.z = q[2]
        # t.transform.rotation.w = q[3]
        t.transform.rotation.x = 0
        t.transform.rotation.y = 0
        t.transform.rotation.z = 0.71
        t.transform.rotation.w = 0.71
        # ---------
        posBall.header.frame_id = 'map'
        posBall.header.stamp = rospy.Time.now()
        posBall.pose.position.x = X
        posBall.pose.position.y = Y
        # posBall.pose.position.x = 0.3
        # posBall.pose.position.y = 1.8
        posBall.pose.position.z = 0.0
        posBall.pose.orientation.x = 0
        posBall.pose.orientation.y = 0
        posBall.pose.orientation.z = 0.71
        posBall.pose.orientation.w = 0.71
        Ballpub.publish(posBall)
    br.sendTransform(t)


if __name__ == '__main__':
    rospy.init_node('tf2_ball_broadcaster')
    turtlename = rospy.get_param('~balls')
    # rospy.Subscriber('enco_value',
    #                  encoder,
    #                  handle_robot_pose)
    rospy.Subscriber('ballPos_topic',
                     Pose,
                     handle_ball_pose,
                     turtlename)
    rospy.Subscriber('robot_pos',
                     Pose,
                     handle_robot_pose)
    
    # rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=10)
    rospy.spin()