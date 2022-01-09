#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data

if __name__ == '__main__':
    rospy.init_node('rannsuu_rate')
    sub = rospy.Subscriber('rand', Int32, cb)
    pub = rospy.Publisher('rand_rate', Int32, queue_size=1)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():

        if n == 1:
            print('トゥース！！！！！！！！！！\n')

        pub.publish(n)
        rate.sleep()
