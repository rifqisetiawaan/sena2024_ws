#!/usr/bin/env python3
import rospy
import tf2_ros
import geometry_msgs.msg
from std_msgs.msg import Float32
from robot_tf_pkg.msg import encoder
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped
import math
import numpy as np

class BallBroadcaster:
    def __init__(self):
        rospy.init_node('tf2_ball_broadcaster')
        self.turtlename = rospy.get_param('~balls')
        self.xpos = 0
        self.ypos = 0
        
        self.ball_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        
        rospy.Subscriber('ballPos_topic', Pose, self.handle_ball_pose)
        rospy.Subscriber('robot_pos', Pose, self.handle_robot_pose)
        
    def handle_robot_pose(self, msg):
        self.xpos = msg.position.x
        self.ypos = msg.position.y
    
    def handle_ball_pose(self, msg):
        br = tf2_ros.TransformBroadcaster()
        t = geometry_msgs.msg.TransformStamped()
        posBall = PoseStamped()
        
        # x = self.xpos/1000 
        # y = self.ypos/1000 
        x = self.xpos/100 + ((msg.position.x)/100)
        y = self.ypos/100 + ((msg.position.y)/100)

        # Rotate coordinates by 90 degrees counterclockwise
        x_rotated = y
        y_rotated = x

        if msg.position.x == 0 and msg.position.y == 0:
            t.header.stamp = rospy.Time.now()
            t.header.frame_id = "map"
            t.child_frame_id = self.turtlename
            t.transform.translation.x = self.xpos
            t.transform.translation.y = self.ypos
            t.transform.translation.z = 0.0
            t.transform.rotation.x = 0
            t.transform.rotation.y = 0
            t.transform.rotation.z = 0
            t.transform.rotation.w = 1
            
            posBall.header.frame_id = 'map'
            posBall.header.stamp = rospy.Time.now()
            posBall.pose.position.x = self.xpos
            posBall.pose.position.y = self.ypos
            posBall.pose.position.z = 0.0
            posBall.pose.orientation.x = 0
            posBall.pose.orientation.y = 0
            posBall.pose.orientation.z = 0
            posBall.pose.orientation.w = 1
            self.ball_pub.publish(posBall)
        else:
            t.header.stamp = rospy.Time.now()
            t.header.frame_id = "map"
            t.child_frame_id = self.turtlename
            t.transform.translation.x = x_rotated
            t.transform.translation.y = y_rotated
            t.transform.translation.z = 0.0
            t.transform.rotation.x = 0
            t.transform.rotation.y = 0
            t.transform.rotation.z = 0
            t.transform.rotation.w = 1
            
            posBall.header.frame_id = 'map'
            posBall.header.stamp = rospy.Time.now()
            posBall.pose.position.x = x_rotated
            posBall.pose.position.y = y_rotated
            posBall.pose.position.z = 0.0
            posBall.pose.orientation.x = 0
            posBall.pose.orientation.y = 0
            posBall.pose.orientation.z = 0
            posBall.pose.orientation.w = 1
            self.ball_pub.publish(posBall)
            
        br.sendTransform(t)

if __name__ == '__main__':
    broadcaster = BallBroadcaster()
    rospy.spin()
