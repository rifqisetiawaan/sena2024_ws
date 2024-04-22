
(cl:in-package :asdf)

(defsystem "camera_yolo-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "yoloPos" :depends-on ("_package_yoloPos"))
    (:file "_package_yoloPos" :depends-on ("_package"))
  ))