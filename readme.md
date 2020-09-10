the script folder include two python script.
# description
1. **'bag_deal.py'**: read rosbag and filter the GPS-data with threshold and create a new rosbag file with topic '/imu/data' '/velodyne_points' '/GPS_1/fix' '/GPS_2/fix'

2. **'bag_display.py'**: subscribe the GPS topic and draw the trajectory in realtime

# Usage

1. copy the run_py into /catkin_ws/src
2. cd ~/catkin_ws
3. catkin_make
4. source ~/catkin_ws/devel/setup.bash

**for display**
5. cd ~/catkin_ws/src/run_py/scripts
6. rosrun run_py bag_display
7. (new terminal) cd ~/path_to_rosbag/
8. rosbag play -r 10 *.bag

**for rosbag filtering**

set input and output path and threshold in bag_deal.py
the result of trajectory from different threshold are in folder reference_img (05 for 0.5m,50 for 5.0m)


5. cd ~/catkin_ws/src/run_py/scripts
6. rosrun run_py bag_deal
