#!/usr/bin/env python3

import rospy
import tf2_ros
import geometry_msgs.msg
import math
import numpy as np
from robot_tf_pkg.msg import encoder
from tf.transformations import quaternion_from_euler

# Fungsi untuk mengkonversi data encoder menjadi posisi dan orientasi
def handle_turtle_pose(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    # Konversi pulsa ke mm
    dist1 = 2 * math.pi * 50 * (msg.enc1 / 135)
    dist2 = 2 * math.pi * 50 * (msg.enc2 / 135)
    dist3 = 2 * math.pi * 50 * (msg.enc3 / 135)

    # Kalkulasi encoder 3 roda
    vy = dist1 * math.cos(math.radians(30)) - dist2 * math.cos(math.radians(30))
    vx = dist3 - dist1 * math.sin(math.radians(30)) - dist2 * math.sin(math.radians(30))
    vo = -((dist1 / 218) + (dist2 / 218) + (dist3 / 218)) / 3
    vo = math.radians(vo)

    # Koordinat kartesian
    a = np.array([
        [math.cos(vo), -math.sin(vo), 0],
        [math.sin(vo), math.cos(vo), 0],
        [0, 0, 1]
    ])
    b = np.array([vy, vx, vo])
    koor = np.dot(a, b)
    ypos, xpos, theta = koor

    return vx, vy, vo

def broadcast_transforms():
    rospy.init_node('tf_broadcaster')

    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    def encoder_callback(msg):
        xpos, ypos, theta = handle_turtle_pose(msg)

        # Mengirim transformasi dari map ke odom
        current_time = rospy.Time.now()
        t.header.stamp = current_time
        t.header.frame_id = "map"
        t.child_frame_id = "odom"
        t.transform.translation.x = xpos/1000  # Menggunakan xpos untuk x
        t.transform.translation.y = ypos/1000  # Menggunakan ypos untuk y
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        br.sendTransform(t)

        # Mengirim transformasi dari odom ke base_footprint
        t.header.stamp = current_time
        t.header.frame_id = "odom"
        t.child_frame_id = "base_footprint"
        t.transform.translation.x = 0.0  # Asumsi bahwa base_footprint berada tepat di atas odom
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        # q = quaternion_from_euler(0, 0, 0)
        t.transform.rotation.x = 0
        t.transform.rotation.y = 0
        t.transform.rotation.z = 0
        t.transform.rotation.w = 1

        br.sendTransform(t)

        # Mengirim transformasi dari base_footprint ke base_link
        t.header.stamp = current_time
        t.header.frame_id = "base_footprint"
        t.child_frame_id = "base_link"
        t.transform.translation.x = 0.0  # Asumsi bahwa base_link berada tepat di atas base_footprint
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        q = quaternion_from_euler(0, 0, math.degrees(theta))
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        br.sendTransform(t)

    # Subscriber untuk encoder data
    rospy.Subscriber('enco_value', encoder, encoder_callback)  # Gantilah 'encoder_topic' dan EncoderMsg sesuai dengan topik dan tipe pesan Anda

    rospy.spin()

if __name__ == '__main__':
    try:
        broadcast_transforms()
    except rospy.ROSInterruptException:
        pass
