;; Auto-generated. Do not edit!


(when (boundp 'prcs_image::squareInfo)
  (if (not (find-package "PRCS_IMAGE"))
    (make-package "PRCS_IMAGE"))
  (shadow 'squareInfo (find-package "PRCS_IMAGE")))
(unless (find-package "PRCS_IMAGE::SQUAREINFO")
  (make-package "PRCS_IMAGE::SQUAREINFO"))

(in-package "ROS")
;;//! \htmlinclude squareInfo.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass prcs_image::squareInfo
  :super ros::object
  :slots (_Header _x1 _y1 _x2 _y2 ))

(defmethod prcs_image::squareInfo
  (:init
   (&key
    ((:Header __Header) (instance std_msgs::Header :init))
    ((:x1 __x1) (instance std_msgs::Int32 :init))
    ((:y1 __y1) (instance std_msgs::Int32 :init))
    ((:x2 __x2) (instance std_msgs::Int32 :init))
    ((:y2 __y2) (instance std_msgs::Int32 :init))
    )
   (send-super :init)
   (setq _Header __Header)
   (setq _x1 __x1)
   (setq _y1 __y1)
   (setq _x2 __x2)
   (setq _y2 __y2)
   self)
  (:Header
   (&rest __Header)
   (if (keywordp (car __Header))
       (send* _Header __Header)
     (progn
       (if __Header (setq _Header (car __Header)))
       _Header)))
  (:x1
   (&rest __x1)
   (if (keywordp (car __x1))
       (send* _x1 __x1)
     (progn
       (if __x1 (setq _x1 (car __x1)))
       _x1)))
  (:y1
   (&rest __y1)
   (if (keywordp (car __y1))
       (send* _y1 __y1)
     (progn
       (if __y1 (setq _y1 (car __y1)))
       _y1)))
  (:x2
   (&rest __x2)
   (if (keywordp (car __x2))
       (send* _x2 __x2)
     (progn
       (if __x2 (setq _x2 (car __x2)))
       _x2)))
  (:y2
   (&rest __y2)
   (if (keywordp (car __y2))
       (send* _y2 __y2)
     (progn
       (if __y2 (setq _y2 (car __y2)))
       _y2)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _Header
    (send _Header :serialization-length)
    ;; std_msgs/Int32 _x1
    (send _x1 :serialization-length)
    ;; std_msgs/Int32 _y1
    (send _y1 :serialization-length)
    ;; std_msgs/Int32 _x2
    (send _x2 :serialization-length)
    ;; std_msgs/Int32 _y2
    (send _y2 :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _Header
       (send _Header :serialize s)
     ;; std_msgs/Int32 _x1
       (send _x1 :serialize s)
     ;; std_msgs/Int32 _y1
       (send _y1 :serialize s)
     ;; std_msgs/Int32 _x2
       (send _x2 :serialize s)
     ;; std_msgs/Int32 _y2
       (send _y2 :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _Header
     (send _Header :deserialize buf ptr-) (incf ptr- (send _Header :serialization-length))
   ;; std_msgs/Int32 _x1
     (send _x1 :deserialize buf ptr-) (incf ptr- (send _x1 :serialization-length))
   ;; std_msgs/Int32 _y1
     (send _y1 :deserialize buf ptr-) (incf ptr- (send _y1 :serialization-length))
   ;; std_msgs/Int32 _x2
     (send _x2 :deserialize buf ptr-) (incf ptr- (send _x2 :serialization-length))
   ;; std_msgs/Int32 _y2
     (send _y2 :deserialize buf ptr-) (incf ptr- (send _y2 :serialization-length))
   ;;
   self)
  )

(setf (get prcs_image::squareInfo :md5sum-) "0704fd39f5e83cde6f6e22cad4f13346")
(setf (get prcs_image::squareInfo :datatype-) "prcs_image/squareInfo")
(setf (get prcs_image::squareInfo :definition-)
      "Header Header
std_msgs/Int32 x1
std_msgs/Int32 y1
std_msgs/Int32 x2
std_msgs/Int32 y2

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: std_msgs/Int32
int32 data
")



(provide :prcs_image/squareInfo "0704fd39f5e83cde6f6e22cad4f13346")


