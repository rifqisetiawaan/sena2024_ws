#!/usr/bin/env python3
import rospy
import tf
from geometry_msgs.msg import Pose

def handle_obs_pose(msg, obstacle):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.position.x , msg.position.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.position.z),
                     rospy.Time.now(),
                     obstacle,
                     "world")

if __name__ == '__main__':
    rospy.init_node('ball_tf_broadcaster')
    obstacle = rospy.get_param('~obstacle')
    rospy.Subscriber('obsPos_topic', Pose, handle_obs_pose, obstacle)
    rospy.spin()