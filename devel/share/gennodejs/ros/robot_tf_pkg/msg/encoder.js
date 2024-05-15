// Auto-generated. Do not edit!

// (in-package robot_tf_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class encoder {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.enc1 = null;
      this.enc2 = null;
      this.enc3 = null;
    }
    else {
      if (initObj.hasOwnProperty('enc1')) {
        this.enc1 = initObj.enc1
      }
      else {
        this.enc1 = 0.0;
      }
      if (initObj.hasOwnProperty('enc2')) {
        this.enc2 = initObj.enc2
      }
      else {
        this.enc2 = 0.0;
      }
      if (initObj.hasOwnProperty('enc3')) {
        this.enc3 = initObj.enc3
      }
      else {
        this.enc3 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type encoder
    // Serialize message field [enc1]
    bufferOffset = _serializer.float64(obj.enc1, buffer, bufferOffset);
    // Serialize message field [enc2]
    bufferOffset = _serializer.float64(obj.enc2, buffer, bufferOffset);
    // Serialize message field [enc3]
    bufferOffset = _serializer.float64(obj.enc3, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type encoder
    let len;
    let data = new encoder(null);
    // Deserialize message field [enc1]
    data.enc1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [enc2]
    data.enc2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [enc3]
    data.enc3 = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'robot_tf_pkg/encoder';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b4b6d686f22bba1d178b85e292ca0a20';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 enc1
    float64 enc2
    float64 enc3
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new encoder(null);
    if (msg.enc1 !== undefined) {
      resolved.enc1 = msg.enc1;
    }
    else {
      resolved.enc1 = 0.0
    }

    if (msg.enc2 !== undefined) {
      resolved.enc2 = msg.enc2;
    }
    else {
      resolved.enc2 = 0.0
    }

    if (msg.enc3 !== undefined) {
      resolved.enc3 = msg.enc3;
    }
    else {
      resolved.enc3 = 0.0
    }

    return resolved;
    }
};

module.exports = encoder;
