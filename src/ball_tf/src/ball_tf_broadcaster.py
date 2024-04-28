#!/usr/bin/env python3
import rospy
import tf
from geometry_msgs.msg import Pose

def handle_ball_pose(msg, ball):
    br = tf.TransformBroadcaster()
    # br.sendTransform((msg.x, msg.y, 0),
    #                  tf.transformations.quaternion_from_euler(0, 0, msg.theta),
    #                  rospy.Time.now(),
    #                  ball,
    #                  "world")
    br.sendTransform((msg.position.x , msg.position.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.position.z),
                     rospy.Time.now(),
                     ball,
                     "world")

if __name__ == '__main__':
    rospy.init_node('ball_tf_broadcaster')
    ball = rospy.get_param('~ball')
    # turtlename = rospy.get_param('~turtle')
    # rospy.Subscriber('/%s/pose' % turtlename,
    #                  turtlesim.msg.Pose,
    #                  handle_ball_pose,
    #                  turtlename)
    rospy.Subscriber('ballPos_topic', Pose, handle_ball_pose, ball)
    rospy.spin()