#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
rospy.init_node('niryo_one_example_python_api')

n = NiryoOne()

try:
    n.activate_learning_mode(False)
    n.move_joints([0,0.64,-1.397,0,0,0])
    n.activate_learning_mode(True)
    print "In rest position!"

except NiryoOneException as e:
    print e

print "--- End"
