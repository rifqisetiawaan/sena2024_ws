#!/usr/bin/env python3

# cam stream program, pub ke yolo_dist
import rospy
import numpy as np
from geometry_msgs.msg import Pose
from open_base.msg import Movement
import math
import cv2
from prcs_image.msg import squareInfo
from prcs_image.image_process import process_img as pr
from prcs_image.command_vel import velo as vl
from ultralytics import YOLO
from prcs_image.msg import yoloPos

def publish_message():
    Ballpub = rospy.Publisher('ballPos_topic', Pose, queue_size=10)
    Obspub = rospy.Publisher('obsPos_topic', Pose, queue_size=10)
    rospy.init_node('camera_yolo', anonymous=False)
    
    rate = rospy.Rate(10)

    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    model = YOLO('/home/krsbi/sena2024_ws/src/camera_yolo/src/script/best.pt')
    poseBall = Pose()
    poseObs = Pose()
    while not rospy.is_shutdown():
        # capture frame by frame
        ret, frame = cap.read()

        if ret==True:
            # rospy.loginfo('publishing video frame')
            
            results = model(frame, conf=0.8)
            frame = results[0].plot()
            # Extract bounding boxes, classes, names, and confidences
            boxes = results[0].boxes.xyxy.tolist()
            classes = results[0].boxes.cls.tolist()
            names = results[0].names
            confidences = max([results[0].boxes.conf.tolist()])
            # plot titik tengah kamera
            cv2.circle(frame, (300, 240), 
                    radius=30, color=(0, 0, 255), thickness=1)

            # Iterate through the results
            for box, cls, conf in zip(boxes, classes, confidences):
                x1, y1, x2, y2 = box
                confidence = conf
                detected_class = cls
                name = names[int(cls)]
                print("----START----")
                # print("BOX----")
                # print(box)
                print("CLS----")
                print(cls)
                # print("CONF---")
                # print(conf)
                # print("----END----")

                if classes == [1.0, 0.0]:
                    # hitung centroid bola
                    x1b, y1b, x2b, y2b = boxes[1]
                    cent_bola = pr.process_image.find_centroid(x1b, y1b, x2b, y2b)
                    
                    # hitung centroid kotak
                    x1k, y1k, x2k, y2k = boxes[0]
                    cent_kotak = pr.process_image.find_centroid(x1k, y1k, x2k, y2k)
                    # plot hasil centroid
                    pr.process_image.plot_line(frame, cent_bola)
                    pr.process_image.plot_line(frame, cent_kotak)
                    print(str(cent_bola)+str(cent_kotak))
                    cbx, cby = cent_bola
                    ckx, cky = cent_kotak
                    # lempar ke message Point32 hasil centroid
                    poseBall.position.x = cbx
                    poseBall.position.y = cby
                    poseObs.position.x = ckx
                    poseObs.position.y = cky
                elif classes == [0.0, 1.0]:
                    # hitung centroid bola
                    x1b, y1b, x2b, y2b = boxes[0]
                    cent_bola = pr.process_image.find_centroid(x1b, y1b, x2b, y2b)
                    
                    # hitung centroid kotak
                    x1k, y1k, x2k, y2k = boxes[1]
                    cent_kotak = pr.process_image.find_centroid(x1k, y1k, x2k, y2k)
                    # plot hasil centroid
                    pr.process_image.plot_line(frame, cent_bola)
                    pr.process_image.plot_line(frame, cent_kotak)
                    print(str(cent_bola)+str(cent_kotak))
                    cbx, cby = cent_bola
                    ckx, cky = cent_kotak
                    # lempar ke message Point32 hasil centroid bola
                    poseBall.position.x = cbx
                    poseBall.position.y = cby
                    poseObs.position.x = ckx
                    poseObs.position.y = cky

                elif classes == [0.0]:
                    # hitung centroid bola
                    x1b, y1b, x2b, y2b = boxes[0]
                    cent_bola = pr.process_image.find_centroid(x1b, y1b, x2b, y2b)
                    
                    # plot hasil centroid
                    pr.process_image.plot_line(frame, cent_bola)
                    print(str(cent_bola))
                    cbx, cby = cent_bola
                    # lempar ke message Point32 hasil centroid bola
                    poseBall.position.x = cbx
                    poseBall.position.y = cby
                    poseObs.position.x = 0.0
                    poseObs.position.y = 0.0

                else:
                    poseBall.position.x = 0.0
                    poseBall.position.y = 0.0
                    poseObs.position.x = 0.0
                    poseObs.position.y = 0.0


            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", frame)
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            # publish message
            Ballpub.publish(poseBall)
            Obspub.publish(poseObs)

        rate.sleep()
        

if __name__ == '__main__':
    try:
        publish_message()
    except rospy.ROSInterruptException:
        pass

# run sebelum dibuat roslaunch:
# rosrun camera_yolo camera_yolo.py
# rosrun rosserial_arduino serial_node.py _port:=/dev/ttyUSB1
# rostopic echo /video_topic