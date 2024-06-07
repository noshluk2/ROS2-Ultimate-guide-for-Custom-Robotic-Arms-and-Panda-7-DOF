# ROS Ultimate guide for Custom Robotic Arms and Panda 7 DOF

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-this-Repository">About This Repository</a></li>
    <li><a href="#Using-this-Repository">Using this Repository</a></li>
    <li><a href="#Course-Workflow">Course Workflow</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Pre-Course-Requirments">Pre-Course Requirments</a></li>
    <li><a href="#Notes">Notes</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>

## About this Repository
This is repository for the course **ROS2 Ultimate guide for Custom Robotic Arms and Panda 7 DOF** availble at Udemy . All the codes are open sourced . Notes are also added in root of the repo.

 ![alt text](https://github.com/noshluk2/ROS2-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF/blob/master/Images/thumbnail.png)
- **[[Get course Access]](https://robotisim.com/project-based-course/)**
----
## Using this Repository
* Install Dependencies
 ```
 sudo apt install ros-<distro>-libfranka ros-<distro>-franka-ros

## for noetic
 sudo apt install ros-noetic-libfranka ros-noetic-franka-ros 
  ```
* Move into your workspace/src folder
 ```
 cd path/to/ros2_ws/src/
##e.g cd ~/ros2_ws/src/
  ```
* Clone the repository in your workspace
```
git clone https://github.com/noshluk2/ROS2-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF
```


* Perform make and build through catkin
 ```
 cd /path/to/workspace_root/
 ##e.g ~/ros2_ws/
 colcon build
 ```

* Source your Workspace in any terminal you open to Run files from this workspace ( which is a basic thing of ROS )
```
source /path/to/ws/devel/setup.bash
```

## Course Workflow
- We will start by creating a custom robot named as BAZU . Which will be created from scratch , URDF containing joints, links are going to be explored in depth. Once the robotic arm will be created we will add Controllers into it (position, effort, Joint Trajectory) from ros_control package .This will lead us to DH tables for forward and inverse kinematics solutions for our custom robot using Robotics Toolbox by Peter Corke .

- After understanding all the basics of with a Custom Robotic Arm we will move to a very well known commercial robotic arm Franka Emika Panda 7 degree of freedom robotic arm. Our first Object will be to install custom controller into it as we would have learned that in previous sections .Only reason to do that is to be able to control any working URDF robot available . Forward and inverse kinematics will be solved for this robot with the help of robotics tool box mentioned earlier .

- Last thing we will do is to make a action lib interface for Joint Trajectory for panda  robot so we just need to send way points and it moves it's end effect in a shape that we will define .


---
## Features
* **Building Custom Robotic Arm**
  -  ![alt text](https://github.com/noshluk2/ROS2-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF/blob/master/Images/1_custom_arm.gif)
* **Controllers Test**
  -  ![alt text](https://github.com/noshluk2/ROS2-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF/blob/master/Images/2_bazu_controller.gif)
* **Joint Trajectories**
  -  ![alt text](https://github.com/noshluk2/ROS2-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF/blob/master/Images/3_panda_jtc.gif)
* **Multi Goal Trajectories**
  - ![alt text](https://github.com/noshluk2/ROS2-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF/blob/master/Images/4_panda_multi_goal.gif)
*


----
## Pre-Course Requirments

**Software Based**
* Ubuntu 22.04 (LTS)
* ROS2 - Humble
---
## Notes
We have uploaded all the notes made during the lectures of the course so you can get more out of this repository with the instructors Notes. A seperate folder named as **Notes** contain a single PDF carrying all the notes in the root of this repository

----
## License

Distributed under the GNU-GPL License. See `LICENSE` for more information.
