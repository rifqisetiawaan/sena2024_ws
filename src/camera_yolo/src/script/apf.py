#!/usr/bin/env python3
import rospy
from prcs_image.msg import yoloPos
from prcs_image.image_process import process_img as pr
import numpy as np
import cv2
mes = yoloPos()


def callback(data):
    # rospy.loginfo( '\n' +
                #   'x_bola ' + str(data.x_bola) + '\n' +
                #   'y_bola ' + str(data.y_bola)+ '\n' +
                #   'x_kotak ' + str(data.x_kotak) + '\n' +
                #   'y_kotak ' + str(data.y_kotak))
    r = 50
    s = 70

    goal = [data.x_bola, data.y_bola]
    obstacle = [data.x_kotak, data.y_kotak]
    # get goal and obstacle distance
    # dist_goal = np.sqrt((goal[0]-0)**2 + ((0-goal[1]))**2)
    # dist_obs  = np.sqrt((obstacle[0]-0)**2 + ((0-obstacle[1]))**2)
    dist_goal = pr.process_image.dist_pixel(300, 245, goal[0], goal[1])
    if obstacle != [0,0]:
        dist_obs = pr.process_image.dist_pixel(300, 245, obstacle[0], obstacle[1])
    elif obstacle == [0,0]:
        dist_obs = 0

    # get theta (angle of attack)
    theta_goal = np.arctan2(goal[1]-0, goal[0]-0)
    theta_obstacle = np.arctan2(obstacle[1]-0, obstacle[0]-0)

    if dist_obs < r:
      delx = np.sign(np.cos(theta_obstacle)) +0
      dely = np.sign(np.cos(theta_obstacle))  +0
    elif dist_obs > r+s:
      delx = 0 +(50 * s *np.cos(theta_obstacle))
      dely = 0 + (50 * s *np.sin(theta_goal))
    elif dist_obs < r+s:
      if delx != 0:
        delx += 50* s *np.cos(theta_goal)
        dely += 50* s *np.sin(theta_goal)
      else:
        delx = 50* s *np.cos(theta_goal)
        dely = 50* s *np.sin(theta_goal)

    rospy.loginfo( '\n' +
                'dist_goal  ' + str(dist_goal) + '\n' +
                'dist_obs ' + str(dist_obs)+ '\n' +
                'theta_goal ' + str(theta_goal) + '\n' +
                'theta_obs ' + str(theta_obstacle))
    

def listener():
    # global msg
    msg = yoloPos()
    rospy.init_node('APFNode', anonymous=False)
    rospy.Subscriber('video_topic', yoloPos, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass