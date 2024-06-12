;; Auto-generated. Do not edit!


(when (boundp 'robot_tf_pkg::encoder)
  (if (not (find-package "ROBOT_TF_PKG"))
    (make-package "ROBOT_TF_PKG"))
  (shadow 'encoder (find-package "ROBOT_TF_PKG")))
(unless (find-package "ROBOT_TF_PKG::ENCODER")
  (make-package "ROBOT_TF_PKG::ENCODER"))

(in-package "ROS")
;;//! \htmlinclude encoder.msg.html


(defclass robot_tf_pkg::encoder
  :super ros::object
  :slots (_enc1 _enc2 _enc3 ))

(defmethod robot_tf_pkg::encoder
  (:init
   (&key
    ((:enc1 __enc1) 0.0)
    ((:enc2 __enc2) 0.0)
    ((:enc3 __enc3) 0.0)
    )
   (send-super :init)
   (setq _enc1 (float __enc1))
   (setq _enc2 (float __enc2))
   (setq _enc3 (float __enc3))
   self)
  (:enc1
   (&optional __enc1)
   (if __enc1 (setq _enc1 __enc1)) _enc1)
  (:enc2
   (&optional __enc2)
   (if __enc2 (setq _enc2 __enc2)) _enc2)
  (:enc3
   (&optional __enc3)
   (if __enc3 (setq _enc3 __enc3)) _enc3)
  (:serialization-length
   ()
   (+
    ;; float32 _enc1
    4
    ;; float32 _enc2
    4
    ;; float32 _enc3
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _enc1
       (sys::poke _enc1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _enc2
       (sys::poke _enc2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _enc3
       (sys::poke _enc3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _enc1
     (setq _enc1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _enc2
     (setq _enc2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _enc3
     (setq _enc3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get robot_tf_pkg::encoder :md5sum-) "3b2d18c22293b69b292f5376e68afd3d")
(setf (get robot_tf_pkg::encoder :datatype-) "robot_tf_pkg/encoder")
(setf (get robot_tf_pkg::encoder :definition-)
      "float32 enc1
float32 enc2
float32 enc3

")



(provide :robot_tf_pkg/encoder "3b2d18c22293b69b292f5376e68afd3d")


