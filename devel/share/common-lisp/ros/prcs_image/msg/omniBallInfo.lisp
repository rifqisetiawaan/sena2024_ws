; Auto-generated. Do not edit!


(cl:in-package prcs_image-msg)


;//! \htmlinclude omniBallInfo.msg.html

(cl:defclass <omniBallInfo> (roslisp-msg-protocol:ros-message)
  ((Header
    :reader Header
    :initarg :Header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (radius
    :reader radius
    :initarg :radius
    :type cl:float
    :initform 0.0)
   (angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (pos_known
    :reader pos_known
    :initarg :pos_known
    :type cl:boolean
    :initform cl:nil)
   (x_pos
    :reader x_pos
    :initarg :x_pos
    :type cl:integer
    :initform 0)
   (y_pos
    :reader y_pos
    :initarg :y_pos
    :type cl:integer
    :initform 0)
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass omniBallInfo (<omniBallInfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <omniBallInfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'omniBallInfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name prcs_image-msg:<omniBallInfo> is deprecated: use prcs_image-msg:omniBallInfo instead.")))

(cl:ensure-generic-function 'Header-val :lambda-list '(m))
(cl:defmethod Header-val ((m <omniBallInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:Header-val is deprecated.  Use prcs_image-msg:Header instead.")
  (Header m))

(cl:ensure-generic-function 'radius-val :lambda-list '(m))
(cl:defmethod radius-val ((m <omniBallInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:radius-val is deprecated.  Use prcs_image-msg:radius instead.")
  (radius m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <omniBallInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:angle-val is deprecated.  Use prcs_image-msg:angle instead.")
  (angle m))

(cl:ensure-generic-function 'pos_known-val :lambda-list '(m))
(cl:defmethod pos_known-val ((m <omniBallInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:pos_known-val is deprecated.  Use prcs_image-msg:pos_known instead.")
  (pos_known m))

(cl:ensure-generic-function 'x_pos-val :lambda-list '(m))
(cl:defmethod x_pos-val ((m <omniBallInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:x_pos-val is deprecated.  Use prcs_image-msg:x_pos instead.")
  (x_pos m))

(cl:ensure-generic-function 'y_pos-val :lambda-list '(m))
(cl:defmethod y_pos-val ((m <omniBallInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:y_pos-val is deprecated.  Use prcs_image-msg:y_pos instead.")
  (y_pos m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <omniBallInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prcs_image-msg:distance-val is deprecated.  Use prcs_image-msg:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <omniBallInfo>) ostream)
  "Serializes a message object of type '<omniBallInfo>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'radius))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'pos_known) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'x_pos)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y_pos)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <omniBallInfo>) istream)
  "Deserializes a message object of type '<omniBallInfo>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'radius) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'pos_known) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x_pos) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y_pos) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<omniBallInfo>)))
  "Returns string type for a message object of type '<omniBallInfo>"
  "prcs_image/omniBallInfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'omniBallInfo)))
  "Returns string type for a message object of type 'omniBallInfo"
  "prcs_image/omniBallInfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<omniBallInfo>)))
  "Returns md5sum for a message object of type '<omniBallInfo>"
  "e12555c6777f103b129b21a823dbf452")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'omniBallInfo)))
  "Returns md5sum for a message object of type 'omniBallInfo"
  "e12555c6777f103b129b21a823dbf452")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<omniBallInfo>)))
  "Returns full string definition for message of type '<omniBallInfo>"
  (cl:format cl:nil "Header Header~%float32 radius~%float32 angle~%bool pos_known~%~%int32 x_pos~%int32 y_pos~%float32 distance~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'omniBallInfo)))
  "Returns full string definition for message of type 'omniBallInfo"
  (cl:format cl:nil "Header Header~%float32 radius~%float32 angle~%bool pos_known~%~%int32 x_pos~%int32 y_pos~%float32 distance~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <omniBallInfo>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Header))
     4
     4
     1
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <omniBallInfo>))
  "Converts a ROS message object to a list"
  (cl:list 'omniBallInfo
    (cl:cons ':Header (Header msg))
    (cl:cons ':radius (radius msg))
    (cl:cons ':angle (angle msg))
    (cl:cons ':pos_known (pos_known msg))
    (cl:cons ':x_pos (x_pos msg))
    (cl:cons ':y_pos (y_pos msg))
    (cl:cons ':distance (distance msg))
))
