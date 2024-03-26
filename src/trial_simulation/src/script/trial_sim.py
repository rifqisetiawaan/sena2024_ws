#!/usr/bin/env python3
# Simulation node for simulating base movement

import time
import rospy
from prcs_image.command_vel import velo as vl
from open_base.msg import Velocity
from open_base.msg import Movement

def sim_gazebo():
    # pub_sim_left = rospy.Publisher('open_base/left_joint_velocity_controller/command', Velocity, queue_size=100)
    # pub_sim_right = rospy.Publisher('open_base/right_joint_velocity_controller/command', Velocity, queue_size=100)
    # pub_sim_back = rospy.Publisher('open_base/back_joint_velocity_controller/command', Velocity, queue_size=100)
    pub_sim = rospy.Publisher('open_base/command', Movement, queue_size=100)
    rospy.init_node('sim_gazebo_node', anonymous=False)
    vel_sim = Movement()

    simulasixy = [50, 130, -130, -50] # maju, kanan, mundur, kiri

    while not rospy.is_shutdown():
        # ---------
        # for i in (range(-180, 180, 30)):
        vel = vl.velo.kejar(-165, 200)
        kin = vl.velo.inv_motor(vel[0], vel[1])

        print(kin)

        vel_sim.movement = 3

        vel_sim.wheel.v_left = kin[0]
        vel_sim.wheel.v_right = kin[1]
        vel_sim.wheel.v_back = kin[2]

        pub_sim.publish(vel_sim)
        # time.sleep(1)
        

if __name__ == '__main__':
    try:
        sim_gazebo()
    except rospy.ROSInterruptException:
        pass