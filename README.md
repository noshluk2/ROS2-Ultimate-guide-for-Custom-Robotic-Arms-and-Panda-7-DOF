# ROS Ultimate guide for Custom Robotic Arms and Panda 7 DOF

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-this-Repository">About This Repository</a></li>
    <li><a href="#Using-this-Repository">Using this Repository</a></li>
    <li><a href="#Course-Workflow">Course Workflow</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Pre-Course-Requirments">Pre-Course Requirments</a></li>
    <li><a href="#Link-to-the-Course">Link to the Course</a></li>
    <li><a href="#Notes">Notes</a></li>
    <li><a href="#Instructors">Instructors</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>

## About this Repository
This is repository for the course **ROS Ultimate guide for Custom Robotic Arms and Panda 7 DOF** availble at Udemy . All the codes are open sourced . Notes are also attached in root of the repo.

 ![alt text](https://github.com/noshluk2/ROS-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF-/blob/master/Images/mainCover.png)
- **[[Get course Here]](https://www.udemy.com/course/robotics-with-ros-build-robotic-arm-in-gazebo-and-moveit/?couponCode=25F74892A6AA6CCB340F)**
----
## Using this Repository
* Move into your workspace/src folder
 ```
 cd path/to/ros1_ws/src/
##e.g cd ~/catkin_ws/src/
  ```
* Clone the repository in your workspace
```
git clone https://github.com/noshluk2/ROS-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF-
```


* Perform make and build through catkin
 ```
 cd /path/to/workspace_root/
 ##e.g ~/catkin_ws/
 catkin_make
 ```
 
* Source your Workspace in any terminal you open to Run files from this workspace ( which is a basic thing of ROS )
```
source /path/to/catkin-ws/devel/setup.bash
```
- (Optional for Power USERs only) Add source to this workspace into bash file
 ```
echo "source /path/to/catkin-ws/devel/setup.bash" >> ~/.bashrc
 ```
  **NOTE:** This upper command is going to add the source file path into your ~/.bashrc file ( Only perform it once and you know what you are doing).This will save your time when running things from the Workspace

----
## Course Workflow
- We will start by creating a custom robot named as BAZU . Which will be created from scratch , URDF containing joints, links are going to be explored in depth. Once the robotic arm will be created we will add Controllers into it (position, effort, Joint Trajectory) from ros_control package .This will lead us to DH tables for forward and inverse kinematics solutions for our custom robot using Robotics Toolbox by Peter Corke .

- After understanding all the basics of with a Custom Robotic Arm we will move to a very well known commercial robotic arm Franka Emika Panda 7 degree of freedom robotic arm. Our first Object will be to install custom controller into it as we would have learned that in previous sections .Only reason to do that is to be able to control any working URDF robot available . Forward and inverse kinematics will be solved for this robot with the help of robotics tool box mentioned earlier .

- Last thing we will do is to make a action lib interface for Joint Trajectory for panda  robot so we just need to send way points and it moves it's end effect in a shape that we will define .


---
## Features
* **Building Custom Robotic Arm** 
  -  ![alt text](https://github.com/noshluk2/ROS-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF-/blob/master/Images/bazu_urdf.gif)
* **Controllers Test** 
  -  ![alt text](https://github.com/noshluk2/ROS-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF-/blob/master/Images/controller_test.gif)
* **DH Table Derivation** 
  -  ![alt text](https://github.com/noshluk2/ROS-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF-/blob/master/Images/dh_table.gif)
* **Forward and Inverse Kinematics Solutions** 
  -  ![alt text](https://github.com/noshluk2/ROS-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF-/blob/master/Images/fk_ik_.gif)
* **Drawing Shapes**
  - ![alt text](https://github.com/noshluk2/ROS-Ultimate-guide-for-Custom-Robotic-Arms-and-Panda-7-DOF-/blob/master/Images/panda_move.gif)
* 


----
## Pre-Course Requirments 

**Software Based**
* Ubuntu 20.04 (LTS)
* ROS1 - Noetic
---
## Link to the Course
Below is a discounted coupon for people who want to take the course in which more explaination to this code has been added

**[[Get course Here]](https://www.udemy.com/course/robotics-with-ros-build-robotic-arm-in-gazebo-and-moveit/?couponCode=25F74892A6AA6CCB340F)**

----
## Notes
 We have uploaded all the notes made during the lectures of the course so you can get more out of this repository with the instructors Notes. A seperate folder named as **Notes** contain a single PDF carrying all the notes in the root of this repository
----

## Instructors

Muhammad Luqman (ROS Simulation and Control Systems) - [Profile Link](https://www.linkedin.com/in/muhammad-luqman-9b227a11b/)  

----
## License

Distributed under the GNU-GPL License. See `LICENSE` for more information.
