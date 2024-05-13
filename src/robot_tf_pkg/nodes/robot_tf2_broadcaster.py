#!/usr/bin/env python3
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg
from std_msgs.msg import Float32


def handle_turtle_pose(msg, turtlename):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = turtlename
    t.transform.translation.x = msg.data
    t.transform.translation.y = msg.data
    t.transform.translation.z = 0.0
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.data)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_robot_broadcaster')
    turtlename = rospy.get_param('~robot')
    rospy.Subscriber('enco_value',
                     Float32,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()