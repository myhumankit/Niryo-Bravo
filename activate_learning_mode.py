#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *

n = NiryoOne()

try:
    n.activate_learning_mode(True)
    print "Activate learning mode"

except NiryoOneException as e:
    print e

print "--- End"
