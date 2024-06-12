#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Pose
import joblib
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Define the model filename
model_filename = '/home/krsbi/sena2024_ws/src/camera_yolo/src/script/polynomial_regression_model.pkl'
poly_filename = '/home/krsbi/sena2024_ws/src/camera_yolo/src/script/polynomial_features.pkl'

# Load the model and polynomial features
model = joblib.load(model_filename)
poly = joblib.load(poly_filename)
message = Pose()

def predict_real_cm(px_x, px_y):
    # Transform the input pixel value to polynomial features
    pixel_value_poly_x = poly.transform([[px_x]])
    pixel_value_poly_y = poly.transform([[px_y]])
    # Make a prediction using the loaded model
    real_cm_x = model.predict(pixel_value_poly_x)[0]
    real_cm_y = model.predict(pixel_value_poly_y)[0]
    return real_cm_x, real_cm_y

def callback(data):
    pub = rospy.Publisher('real_cm_topic', Pose, queue_size=10)
    rate = rospy.Rate(10)
    pixel_value_x = data.position.x
    pixel_value_y = data.position.y
    real_cm = predict_real_cm(pixel_value_x, pixel_value_y)
    real_x, real_y = real_cm
    message.position.x = real_x
    message.position.y = real_y
    pub.publish(message)

def camera_calibration_node():
    rospy.init_node('camera_calibration_node', anonymous=False)
    rospy.Subscriber('ballPos_topic', Pose, callback)    
    rospy.spin()
    

if __name__ == '_main_':
    try:
        camera_calibration_node()
    except rospy.ROSInterruptException:
        pass