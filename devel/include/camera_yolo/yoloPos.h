// Generated by gencpp from file camera_yolo/yoloPos.msg
// DO NOT EDIT!


#ifndef CAMERA_YOLO_MESSAGE_YOLOPOS_H
#define CAMERA_YOLO_MESSAGE_YOLOPOS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace camera_yolo
{
template <class ContainerAllocator>
struct yoloPos_
{
  typedef yoloPos_<ContainerAllocator> Type;

  yoloPos_()
    : x_bola(0.0)
    , y_bola(0.0)
    , x_kotak(0.0)
    , y_kotak(0.0)  {
    }
  yoloPos_(const ContainerAllocator& _alloc)
    : x_bola(0.0)
    , y_bola(0.0)
    , x_kotak(0.0)
    , y_kotak(0.0)  {
  (void)_alloc;
    }



   typedef double _x_bola_type;
  _x_bola_type x_bola;

   typedef double _y_bola_type;
  _y_bola_type y_bola;

   typedef double _x_kotak_type;
  _x_kotak_type x_kotak;

   typedef double _y_kotak_type;
  _y_kotak_type y_kotak;





  typedef boost::shared_ptr< ::camera_yolo::yoloPos_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::camera_yolo::yoloPos_<ContainerAllocator> const> ConstPtr;

}; // struct yoloPos_

typedef ::camera_yolo::yoloPos_<std::allocator<void> > yoloPos;

typedef boost::shared_ptr< ::camera_yolo::yoloPos > yoloPosPtr;
typedef boost::shared_ptr< ::camera_yolo::yoloPos const> yoloPosConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::camera_yolo::yoloPos_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::camera_yolo::yoloPos_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::camera_yolo::yoloPos_<ContainerAllocator1> & lhs, const ::camera_yolo::yoloPos_<ContainerAllocator2> & rhs)
{
  return lhs.x_bola == rhs.x_bola &&
    lhs.y_bola == rhs.y_bola &&
    lhs.x_kotak == rhs.x_kotak &&
    lhs.y_kotak == rhs.y_kotak;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::camera_yolo::yoloPos_<ContainerAllocator1> & lhs, const ::camera_yolo::yoloPos_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace camera_yolo

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::camera_yolo::yoloPos_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::camera_yolo::yoloPos_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::camera_yolo::yoloPos_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::camera_yolo::yoloPos_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::camera_yolo::yoloPos_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::camera_yolo::yoloPos_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::camera_yolo::yoloPos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "01818e6dac8eb5be630fe9157773ca48";
  }

  static const char* value(const ::camera_yolo::yoloPos_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x01818e6dac8eb5beULL;
  static const uint64_t static_value2 = 0x630fe9157773ca48ULL;
};

template<class ContainerAllocator>
struct DataType< ::camera_yolo::yoloPos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "camera_yolo/yoloPos";
  }

  static const char* value(const ::camera_yolo::yoloPos_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::camera_yolo::yoloPos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 x_bola\n"
"float64 y_bola\n"
"float64 x_kotak\n"
"float64 y_kotak\n"
;
  }

  static const char* value(const ::camera_yolo::yoloPos_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::camera_yolo::yoloPos_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x_bola);
      stream.next(m.y_bola);
      stream.next(m.x_kotak);
      stream.next(m.y_kotak);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct yoloPos_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::camera_yolo::yoloPos_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::camera_yolo::yoloPos_<ContainerAllocator>& v)
  {
    s << indent << "x_bola: ";
    Printer<double>::stream(s, indent + "  ", v.x_bola);
    s << indent << "y_bola: ";
    Printer<double>::stream(s, indent + "  ", v.y_bola);
    s << indent << "x_kotak: ";
    Printer<double>::stream(s, indent + "  ", v.x_kotak);
    s << indent << "y_kotak: ";
    Printer<double>::stream(s, indent + "  ", v.y_kotak);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CAMERA_YOLO_MESSAGE_YOLOPOS_H
