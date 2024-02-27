; Auto-generated. Do not edit!


(cl:in-package prcs_image-msg)


;//! \htmlinclude squareInfo.msg.html

(cl:defclass <squareInfo> (roslisp-msg-protocol:ros-message)
  ((Header
    :reader Header
    :initarg :Header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (x1
    :reader x1
    :initarg :x1
    :type std_msgs-msg:Int32
    :initform (cl:make-instance 'std_msgs-msg:Int32))
   (y1
    :reader y1
    :initarg :y1
    :type std_msgs-msg:Int32
    :initform (cl:make-instance 'std_msgs-msg:Int32))
   (x2
    :reader x2
    :initarg :x2
    :type std_msgs-msg:Int32
    :initform (cl:make-instance 'std_msgs-msg:Int32))
   (y2
    :reader y2
    :initarg :y2
    :type std_msgs-msg:Int32
    :initform (cl:make-instance 'std_msgs-msg:Int32)))
)

(cl:defclass squareInfo (<squareInfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <squareInfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'squareInfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name prcs_image-msg:<squareInfo> is deprecated: use prcs_image-msg:squareInfo instead.")))

(cl:ensure-generic-function 'Header-val :lambda-list '(m))
(cl:defmethod Header-val ((m <squareInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:Header-val is deprecated.  Use prcs_image-msg:Header instead.")
  (Header m))

(cl:ensure-generic-function 'x1-val :lambda-list '(m))
(cl:defmethod x1-val ((m <squareInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:x1-val is deprecated.  Use prcs_image-msg:x1 instead.")
  (x1 m))

(cl:ensure-generic-function 'y1-val :lambda-list '(m))
(cl:defmethod y1-val ((m <squareInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:y1-val is deprecated.  Use prcs_image-msg:y1 instead.")
  (y1 m))

(cl:ensure-generic-function 'x2-val :lambda-list '(m))
(cl:defmethod x2-val ((m <squareInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:x2-val is deprecated.  Use prcs_image-msg:x2 instead.")
  (x2 m))

(cl:ensure-generic-function 'y2-val :lambda-list '(m))
(cl:defmethod y2-val ((m <squareInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:y2-val is deprecated.  Use prcs_image-msg:y2 instead.")
  (y2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <squareInfo>) ostream)
  "Serializes a message object of type '<squareInfo>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'x1) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'y1) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'x2) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'y2) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <squareInfo>) istream)
  "Deserializes a message object of type '<squareInfo>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'x1) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'y1) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'x2) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'y2) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<squareInfo>)))
  "Returns string type for a message object of type '<squareInfo>"
  "prcs_image/squareInfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'squareInfo)))
  "Returns string type for a message object of type 'squareInfo"
  "prcs_image/squareInfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<squareInfo>)))
  "Returns md5sum for a message object of type '<squareInfo>"
  "0704fd39f5e83cde6f6e22cad4f13346")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'squareInfo)))
  "Returns md5sum for a message object of type 'squareInfo"
  "0704fd39f5e83cde6f6e22cad4f13346")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<squareInfo>)))
  "Returns full string definition for message of type '<squareInfo>"
  (cl:format cl:nil "Header Header~%std_msgs/Int32 x1~%std_msgs/Int32 y1~%std_msgs/Int32 x2~%std_msgs/Int32 y2~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: std_msgs/Int32~%int32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'squareInfo)))
  "Returns full string definition for message of type 'squareInfo"
  (cl:format cl:nil "Header Header~%std_msgs/Int32 x1~%std_msgs/Int32 y1~%std_msgs/Int32 x2~%std_msgs/Int32 y2~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: std_msgs/Int32~%int32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <squareInfo>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'x1))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'y1))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'x2))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'y2))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <squareInfo>))
  "Converts a ROS message object to a list"
  (cl:list 'squareInfo
    (cl:cons ':Header (Header msg))
    (cl:cons ':x1 (x1 msg))
    (cl:cons ':y1 (y1 msg))
    (cl:cons ':x2 (x2 msg))
    (cl:cons ':y2 (y2 msg))
))
