#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('rannsuu')
pub = rospy.Publisher('rand', Int32, queue_size=1)
rate = rospy.Rate(1)
n = 0
while not rospy.is_shutdown():
    n = random.randint(1,100)

    if n == 1:
        rate = rospy.Rate(1)

    else:
        rate = rospy.Rate(50)

    pub.publish(n)
    rate.sleep()
