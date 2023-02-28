#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import NavSatFix
from piksi_rtk_msgs.msg import WMUNavSatFix

pub = rospy.Publisher("gps/fix", NavSatFix, queue_size=10)

def callback(gnss_msg):
    
    navsat_msg = NavSatFix()

    navsat_msg.header = gnss_msg.header
    navsat_msg.status = gnss_msg.status
    navsat_msg.latitude = gnss_msg.latitude
    navsat_msg.longitude = gnss_msg.longitude
    navsat_msg.altitude = gnss_msg.altitude
    navsat_msg.position_covariance = gnss_msg.position_covariance
    navsat_msg.position_covariance_type = gnss_msg.position_covariance_type

    pub.publish(navsat_msg)

def main():
    
    rospy.init_node("pass_gnss_node")

    rospy.loginfo("Starting gnss node.")

    rospy.Subscriber("piksi_multi_base_station/navsatfix_rtk_fix", WMUNavSatFix, callback)

    rospy.spin()

try:
    main()
except KeyboardInterrupt:
    pass