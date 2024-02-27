// Auto-generated. Do not edit!

// (in-package prcs_image.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class squareInfo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Header = null;
      this.x1 = null;
      this.y1 = null;
      this.x2 = null;
      this.y2 = null;
    }
    else {
      if (initObj.hasOwnProperty('Header')) {
        this.Header = initObj.Header
      }
      else {
        this.Header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('x1')) {
        this.x1 = initObj.x1
      }
      else {
        this.x1 = new std_msgs.msg.Int32();
      }
      if (initObj.hasOwnProperty('y1')) {
        this.y1 = initObj.y1
      }
      else {
        this.y1 = new std_msgs.msg.Int32();
      }
      if (initObj.hasOwnProperty('x2')) {
        this.x2 = initObj.x2
      }
      else {
        this.x2 = new std_msgs.msg.Int32();
      }
      if (initObj.hasOwnProperty('y2')) {
        this.y2 = initObj.y2
      }
      else {
        this.y2 = new std_msgs.msg.Int32();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type squareInfo
    // Serialize message field [Header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.Header, buffer, bufferOffset);
    // Serialize message field [x1]
    bufferOffset = std_msgs.msg.Int32.serialize(obj.x1, buffer, bufferOffset);
    // Serialize message field [y1]
    bufferOffset = std_msgs.msg.Int32.serialize(obj.y1, buffer, bufferOffset);
    // Serialize message field [x2]
    bufferOffset = std_msgs.msg.Int32.serialize(obj.x2, buffer, bufferOffset);
    // Serialize message field [y2]
    bufferOffset = std_msgs.msg.Int32.serialize(obj.y2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type squareInfo
    let len;
    let data = new squareInfo(null);
    // Deserialize message field [Header]
    data.Header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [x1]
    data.x1 = std_msgs.msg.Int32.deserialize(buffer, bufferOffset);
    // Deserialize message field [y1]
    data.y1 = std_msgs.msg.Int32.deserialize(buffer, bufferOffset);
    // Deserialize message field [x2]
    data.x2 = std_msgs.msg.Int32.deserialize(buffer, bufferOffset);
    // Deserialize message field [y2]
    data.y2 = std_msgs.msg.Int32.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.Header);
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'prcs_image/squareInfo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0704fd39f5e83cde6f6e22cad4f13346';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header Header
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new squareInfo(null);
    if (msg.Header !== undefined) {
      resolved.Header = std_msgs.msg.Header.Resolve(msg.Header)
    }
    else {
      resolved.Header = new std_msgs.msg.Header()
    }

    if (msg.x1 !== undefined) {
      resolved.x1 = std_msgs.msg.Int32.Resolve(msg.x1)
    }
    else {
      resolved.x1 = new std_msgs.msg.Int32()
    }

    if (msg.y1 !== undefined) {
      resolved.y1 = std_msgs.msg.Int32.Resolve(msg.y1)
    }
    else {
      resolved.y1 = new std_msgs.msg.Int32()
    }

    if (msg.x2 !== undefined) {
      resolved.x2 = std_msgs.msg.Int32.Resolve(msg.x2)
    }
    else {
      resolved.x2 = new std_msgs.msg.Int32()
    }

    if (msg.y2 !== undefined) {
      resolved.y2 = std_msgs.msg.Int32.Resolve(msg.y2)
    }
    else {
      resolved.y2 = new std_msgs.msg.Int32()
    }

    return resolved;
    }
};

module.exports = squareInfo;
