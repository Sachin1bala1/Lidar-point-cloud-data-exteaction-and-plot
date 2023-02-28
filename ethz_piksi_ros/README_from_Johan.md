Procedure for GPS data collection process.

I forgot to mention that I modified the ros message type for the GPS sensor
on the vehicle (therefore it is using a custom message). If you do rostopic info
on the ropic you will see it is message type WMUNavSatFix. So to keep everything
on the standard format, I created a pass_gps.py file that gets the data from my 
custom message and publishes it into the standard sensor_msgs/NavSatFix format. Also, you need the GPS ROS driver to read the information from the sensor because their driver uses a custom message called piksi_rtk_msgs/NavSatFix.

Hence, to read the data from the GPS sensor you need to first:
-Download and compile the GPS ROS driver to your ROS workspace(I uploaded the driver to google drive).
-After everything compiled run the rosbag, run the pass_gps.py and then run the collect_gps.py file.

If you use the carla ROS bag I uploaded, you don't have to do any of this because carla uses the standard ROS messages.

Hence, if you use the carla ROS bag do the following:
-Run rosbag and run collect_gps.py file (don't forget to change the topic name on inside the python file so it subscribes to the correct one).

For the Lidar stuff do

rosrun pcl_ros pointcloud_to_pcd input:=/velodyne/pointcloud2

Change lidar topic name. Also make sure to run this in an empty folder because it stores all the pcd files in your current directory. To visualize the pointcloud using python I recommend using the Open3D library, which is a python library to work with lidar data. There are a bunch of tutorials on how to plot and stuff. I uploaded a simple visualize_pcd.py file that just plots the whole pointcloud (dont forget to change the name of the pcd file).