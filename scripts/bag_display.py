#!/usr/bin/python

# -*- coding: UTF-8 -*-
# this code is for displaying the trajectory
# use "rosbag play *.bag" then run this script to draw trajectory
# cd to the dir of this script then rosrun. otherwise this script cannot find img file
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix,Imu,PointCloud2
import matplotlib.pyplot as plt

threshold_xy = 5
threshold_z = 10

def callback(data):

    covtuple = data.position_covariance
    if covtuple[0] > threshold_xy or covtuple[4] > threshold_xy or covtuple[8] > threshold_z:
        plt.scatter(x=[data.longitude], y=[data.latitude], s=45, c='r')
        data.status.status = -1
    else:
        plt.scatter(x=[data.longitude], y=[data.latitude], s = 45, c='b')
    rospy.loginfo("lat [%f], lon [%f], status [%i], covariance [%f][%f][%f]", data.latitude, data.longitude, data.status.status, covtuple[0], covtuple[4], covtuple[8])
    plt.draw()

def initialisation():

    rospy.init_node('plotGpsDataOnMap')
    rospy.Subscriber("/GPS_1/fix", NavSatFix, callback)

    # adjust these values based on your location and map, lat and long are in decimal degrees
    TRX = 8.451924          #top right longitude
    TRY = 49.020612           #top right latitude
    BLX = 8.402887          #bottom left longitude
    BLY = 49.000618             #bottom left latitude
    mapFile = 'mymap.png'
    imgMap = 0
    #now plot the data on a graph
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('POSITION (in Decimal Degrees)')

    #display the image under the graph
    #read a png file to map on
    imgMap = plt.imread(mapFile)
    implot = plt.imshow(imgMap,extent=[BLX, TRX, BLY, TRY],aspect = 'auto')
    plt.show()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    initialisation()






