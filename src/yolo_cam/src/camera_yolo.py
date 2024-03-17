#!/usr/bin/env python3

# cam stream program, pub ke yolo_dist
import rospy
from sensor_msgs.msg import Image
import math
import cv2
from prcs_image.msg import squareInfo
from prcs_image.image_process import process_img as pr
from prcs_image.command_vel import velo as vl
from ultralytics import YOLO

def publish_message():
    pub = rospy.Publisher('video_topic', squareInfo, queue_size=10)
    rospy.init_node('webcam_stream', anonymous=False)
    
    rate = rospy.Rate(10)

    cap = cv2.VideoCapture(0)
    model = YOLO('/home/krsbi/sena2024_ws/src/yolo_cam/src/best.pt')
    sq = squareInfo()
    while not rospy.is_shutdown():
        # capture frame by frame
        ret, frame = cap.read()
        # frame = imutils.resize(frame, width=480)
        

        if ret==True:
            # rospy.loginfo('publishing video frame')
            
            results = model(frame, conf=0.85)
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
                
            
            if classes == [0.0]:
                # print("%.2f" % confidence)
                # print('----------')

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
                    print(vel)

                    # kinematika motor
                    kin = vl.velo.inv_motor(vel[0], vel[1])
                    print(kin)

                    # Use putText() method for inserting text on video
                    pr.process_image.text_display_det(frame, ang, dist_real, vel)
                    
                    sq.x1.data = int(x1)
                    sq.x2.data = int(x2)
                    sq.y1.data = int(y1)
                    sq.y2.data = int(y2)
            
            else:
                sq.x1.data = 0
                sq.x2.data = 0
                sq.y1.data = 0
                sq.y2.data = 0

                pr.process_image.text_display_na(frame)                

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            # publish and convert img to ros format
            # pub.publish(br.cv2_to_imgmsg(frame, 'bgr8'))
            pub.publish(sq)
        rate.sleep()
        

if __name__ == '__main__':
    try:
        publish_message()
    except rospy.ROSInterruptException:
        pass