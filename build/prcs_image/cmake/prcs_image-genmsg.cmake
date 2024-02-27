# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "prcs_image: 2 messages, 0 services")

set(MSG_I_FLAGS "-Iprcs_image:/home/krsbi/sena2024_ws/src/prcs_image/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(prcs_image_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg" NAME_WE)
add_custom_target(_prcs_image_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "prcs_image" "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg" NAME_WE)
add_custom_target(_prcs_image_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "prcs_image" "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg" "std_msgs/Header:std_msgs/Int32"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/prcs_image
)
_generate_msg_cpp(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/prcs_image
)

### Generating Services

### Generating Module File
_generate_module_cpp(prcs_image
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/prcs_image
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(prcs_image_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(prcs_image_generate_messages prcs_image_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_cpp _prcs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_cpp _prcs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(prcs_image_gencpp)
add_dependencies(prcs_image_gencpp prcs_image_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS prcs_image_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/prcs_image
)
_generate_msg_eus(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/prcs_image
)

### Generating Services

### Generating Module File
_generate_module_eus(prcs_image
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/prcs_image
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(prcs_image_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(prcs_image_generate_messages prcs_image_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_eus _prcs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_eus _prcs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(prcs_image_geneus)
add_dependencies(prcs_image_geneus prcs_image_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS prcs_image_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/prcs_image
)
_generate_msg_lisp(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/prcs_image
)

### Generating Services

### Generating Module File
_generate_module_lisp(prcs_image
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/prcs_image
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(prcs_image_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(prcs_image_generate_messages prcs_image_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_lisp _prcs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_lisp _prcs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(prcs_image_genlisp)
add_dependencies(prcs_image_genlisp prcs_image_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS prcs_image_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/prcs_image
)
_generate_msg_nodejs(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/prcs_image
)

### Generating Services

### Generating Module File
_generate_module_nodejs(prcs_image
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/prcs_image
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(prcs_image_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(prcs_image_generate_messages prcs_image_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_nodejs _prcs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_nodejs _prcs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(prcs_image_gennodejs)
add_dependencies(prcs_image_gennodejs prcs_image_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS prcs_image_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/prcs_image
)
_generate_msg_py(prcs_image
  "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/prcs_image
)

### Generating Services

### Generating Module File
_generate_module_py(prcs_image
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/prcs_image
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(prcs_image_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(prcs_image_generate_messages prcs_image_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/omniBallInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_py _prcs_image_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/krsbi/sena2024_ws/src/prcs_image/msg/squareInfo.msg" NAME_WE)
add_dependencies(prcs_image_generate_messages_py _prcs_image_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(prcs_image_genpy)
add_dependencies(prcs_image_genpy prcs_image_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS prcs_image_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/prcs_image)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/prcs_image
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(prcs_image_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/prcs_image)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/prcs_image
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(prcs_image_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/prcs_image)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/prcs_image
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(prcs_image_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/prcs_image)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/prcs_image
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(prcs_image_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/prcs_image)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/prcs_image\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/prcs_image
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(prcs_image_generate_messages_py std_msgs_generate_messages_py)
endif()
