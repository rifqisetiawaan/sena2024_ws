#!/usr/bin/env python3
import rospy
from prcs_image.msg import yoloPos
mes = yoloPos()

def callback(data):
    # global msg
    # rospy.loginfo('x_bola ' + str(mes.x_bola) + '\n' +
    #               'y_bola ' + str(mes.y_bola)+ '\n' +
    #               'x_kotak ' + str(mes.x_kotak) + '\n' +
    #               'y_kotak ' + str(mes.y_kotak))
    rospy.loginfo( '\n' +
                  'x_bola ' + str(data.x_bola) + '\n' +
                  'y_bola ' + str(data.y_bola)+ '\n' +
                  'x_kotak ' + str(data.x_kotak) + '\n' +
                  'y_kotak ' + str(data.y_kotak))

def listener():
    # global msg
    msg = yoloPos()
    rospy.init_node('APFNode', anonymous=False)
    rospy.Subscriber('video_topic', yoloPos, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()