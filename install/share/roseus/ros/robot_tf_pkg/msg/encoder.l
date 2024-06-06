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
    ;; float64 _enc1
    8
    ;; float64 _enc2
    8
    ;; float64 _enc3
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _enc1
       (sys::poke _enc1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _enc2
       (sys::poke _enc2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _enc3
       (sys::poke _enc3 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _enc1
     (setq _enc1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _enc2
     (setq _enc2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _enc3
     (setq _enc3 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get robot_tf_pkg::encoder :md5sum-) "b4b6d686f22bba1d178b85e292ca0a20")
(setf (get robot_tf_pkg::encoder :datatype-) "robot_tf_pkg/encoder")
(setf (get robot_tf_pkg::encoder :definition-)
      "float64 enc1
float64 enc2
float64 enc3
")



(provide :robot_tf_pkg/encoder "b4b6d686f22bba1d178b85e292ca0a20")


