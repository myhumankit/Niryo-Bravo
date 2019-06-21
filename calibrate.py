#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
rospy.init_node('niryo_one_example_python_api')

n = NiryoOne()

try:
    n.calibrate_auto()
    print "Calibration finished !"

except NiryoOneException as e:
    print e

print "--- End"
