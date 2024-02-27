
(cl:in-package :asdf)

(defsystem "prcs_image-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "omniBallInfo" :depends-on ("_package_omniBallInfo"))
    (:file "_package_omniBallInfo" :depends-on ("_package"))
    (:file "squareInfo" :depends-on ("_package_squareInfo"))
    (:file "_package_squareInfo" :depends-on ("_package"))
  ))