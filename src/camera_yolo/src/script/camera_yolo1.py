#!/usr/bin/env python3

# cam stream program, pub ke yolo_dist
import rospy
import numpy as np
from geometry_msgs.msg import Point32
from open_base.msg import Movement
import math
import cv2
# from prcs_image.msg import squareInfo
from prcs_image.image_process import process_img as pr
from prcs_image.command_vel import velo as vl
from ultralytics import YOLO

def publish_message():
    pub = rospy.Publisher('video_topic', Point32, queue_size=10)
    pub_sim = rospy.Publisher('open_base/command', Movement, queue_size=100)
    rospy.init_node('webcam_stream', anonymous=False)
    
    rate = rospy.Rate(10)

    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    model = YOLO('/home/krsbi/sena2024_ws/src/camera_yolo/src/script/best.pt')
    tws = Point32()
    vel_sim = Movement()
    while not rospy.is_shutdown():
        # capture frame by frame
        ret, frame = cap.read()

        if ret==True:
            # rospy.loginfo('publishing video frame')
            
            results = model(frame)
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
                # x1, y1, x2, y2 = boxes[0]
                print(boxes[0])
                print("------")
                # print(cls)
                # print("-------")
                # print(conf)
                confidence = conf
                detected_class = cls
                name = names[int(cls)]

            if classes == [1.0, 0.0] or classes == [0.0, 1.0]:
                x1, y1, x2, y2 = boxes[0]
                # hitung centroid
                centroid = pr.process_image.find_centroid(x1, y1, x2, y2)
                print(centroid)
                cntx, cnty = centroid
                # plot hasil centroid
                pcent = pr.process_image.plot_line(frame, centroid)
                 
                if centroid is not None:
                    # hitung jarak (pixel)
                    dist_px = pr.process_image.dist_pixel(300, 240,
                                                            cntx, cnty)
                    print('ini dist pixel ' + str(dist_px))

                    # hitung jarak real
                    dist_real = pr.process_image.dist_real(dist_px)
                    print('ini dist real ' + str(dist_real))

                    # penentuan angle
                    ang = pr.process_image.penentuan_derajat(cntx, cnty)
                    print(ang)
                    ang = str(ang[3])

                    # penentuan arah gerak
                    vel = vl.velo.kejar(float(ang), float(dist_real))
                    print('Ini Status ----> '+str(vel[0]))

                    # kinematika motor
                    kin = vl.velo.inv_motor(vel[0], vel[1])
                    print('Power Motor '+str(kin))

                    print(fps)

                    # Use putText() method for inserting text on video
                    pr.process_image.text_display_det(frame, ang, dist_real, vel[0], kin, fps)
                    
                    tws.x = kin[0]
                    tws.y = kin[1]
                    tws.z = kin[2]

                    vel_sim.movement = 3
                    vel_sim.wheel.v_right = tws.x
                    vel_sim.wheel.v_left = tws.y
                    vel_sim.wheel.v_back = tws.z
                    
                    # tws.linear = kin
            
            else:
                tws.x = 0
                tws.y = 0
                tws.z = 0

                vel_sim.wheel.v_right = 0
                vel_sim.wheel.v_left = 0
                vel_sim.wheel.v_back = 0
 
                pr.process_image.text_display_na(frame)                

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            # publish and convert img to ros format
            # pub.publish(br.cv2_to_imgmsg(frame, 'bgr8'))
            pub_sim.publish(vel_sim)
            pub.publish(tws)
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