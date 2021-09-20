# ROS1 Ultimate Robotic Arm Course for Begginers with Moveit 
# Repository Under Construction


From Working SOlution:
- Get the two packages from repository and add them to your wokspace then follow "howtoruncommand.txt" file in "franka_gazebo"
- to change the controller type 
-- Change in "panda_arm.urdf.xacro" in franka descriptuion
-- Change config file in franka_gazebo
-- Change launch file gazebo controllers in franka_gazebo
-- Installations :
--- sudo apt install ros-noetic-rqt-reconfigure
--- sudo apt install ros-noetic-dynamic-reconfigure


-------
From Start :
-  Get the franka ros robot here : https://github.com/frankaemika/franka_ros.git
- Remove the unneccesary folders [franka_hw,franka_ros,franka_msgs,control,example controllers]

- remove dependednecies in franka_gazebo cmake to remove last deleted three directories from ""find_plugin"

--------
- Provide the model using
This is the completed Course repository . Files created in the beginning of the course are edited
and this repository contains files we obtained at the completion of the course.

