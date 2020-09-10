#!/usr/bin/python

# -*- coding: UTF-8 -*-
import rosbag
import rospy
# threshold for covariance
# the third value(z) of covariance is always greater than the first(x) and second(y)
threshold_xy = 5
threshold_z = 10
input_bag_path = r'/home/yancheng/KIT_MA/Messdaten/2020_07_16_Testfahrt_KA/CH06US12_Versuchsfahrzeug.bag'
output_bag_path = r'/home/yancheng/KIT_MA/Messdaten/2020_07_16_Testfahrt_KA/CH06US12_Versuchsfahrzeug_filtered.bag'

bag = rosbag.Bag(input_bag_path)
with rosbag.Bag(output_bag_path, 'w') as out_bag:
    for topic, msg, t in bag.read_messages():
        if topic == '/imu/data' or topic == '/velodyne_points':
            out_bag.write(topic, msg, t)
            rospy.loginfo("[%s written ok]",topic)
        if topic == '/GPS_1/fix' or topic == '/GPS_2/fix':
            covtuple = msg.position_covariance
            if covtuple[0] > threshold_xy or covtuple[4] > threshold_xy or covtuple[8] > threshold_z:
                msg.status.status = -1
            out_bag.write(topic, msg, t)
            rospy.loginfo("lat [%f], lon [%f], status [%i], covariance [%f][%f][%f] ,wirtten ok", msg.latitude, msg.longitude,
                          msg.status.status, covtuple[0], covtuple[4], covtuple[8])
