# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from camera_yolo/yoloPos.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class yoloPos(genpy.Message):
  _md5sum = "01818e6dac8eb5be630fe9157773ca48"
  _type = "camera_yolo/yoloPos"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 x_bola
float64 y_bola
float64 x_kotak
float64 y_kotak"""
  __slots__ = ['x_bola','y_bola','x_kotak','y_kotak']
  _slot_types = ['float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x_bola,y_bola,x_kotak,y_kotak

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(yoloPos, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.x_bola is None:
        self.x_bola = 0.
      if self.y_bola is None:
        self.y_bola = 0.
      if self.x_kotak is None:
        self.x_kotak = 0.
      if self.y_kotak is None:
        self.y_kotak = 0.
    else:
      self.x_bola = 0.
      self.y_bola = 0.
      self.x_kotak = 0.
      self.y_kotak = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4d().pack(_x.x_bola, _x.y_bola, _x.x_kotak, _x.y_kotak))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.x_bola, _x.y_bola, _x.x_kotak, _x.y_kotak,) = _get_struct_4d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4d().pack(_x.x_bola, _x.y_bola, _x.x_kotak, _x.y_kotak))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.x_bola, _x.y_bola, _x.x_kotak, _x.y_kotak,) = _get_struct_4d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
