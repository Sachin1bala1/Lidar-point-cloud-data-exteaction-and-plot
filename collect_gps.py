#!/usr/bin/env python3

import rospy
import csv
from sensor_msgs.msg import NavSatFix

rows = []

def callback(msg):
    
    rows.append([msg.header.stamp.to_sec(), msg.latitude, \
        msg.longitude, msg.altitude])

def shutdown():
    
    rospy.loginfo("Writing to CSV...")

    fields = ['time', 'latitude', 'longitude', 'altitude']

    # writing to csv file
    with open( 'gps_points.csv' ,"w") as f:
        # creating a csv writer object
        csvwriter = csv.writer(f)

        # writing the fields 
        csvwriter.writerow(fields)

        csvwriter.writerows(rows)

def main():
    
    rospy.init_node("gps_node")

    rospy.loginfo("Starting node.")

    rospy.on_shutdown(shutdown)

    rospy.Subscriber("/carla/ego_vehicle/gnss", NavSatFix, callback)
    #rospy.Subscriber("gps/fix", NavSatFix, callback)
    rospy.spin()

try:
    main()
except KeyboardInterrupt:
    pass