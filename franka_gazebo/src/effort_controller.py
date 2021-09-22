#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import roboticstoolbox as rtb
from spatialmath import SE3
import numpy as np
import sys

## Giving Two states for robot pose of cup
# rosrun franka_gazebo trajectory_command.py 0.8 0.4 .07 0.04 0.04
# bring it down
# 3- close claws


class Trajectoryfor_pick_and_place():
    def __init__(self):
        rospy.init_node('Panda_Effort_msgs_publisher')
        self.controllers_list = ["/panda/joint%d_controller/command" % x for x in range(9)]
        for index,controller in enumerate(self.controllers_list):
            self.publihser_list[index] = rospy.Publisher(controller,JointTrajectory, queue_size=10)
        
        self.panda_joints = ['panda_joint1','panda_joint2','panda_joint3','panda_joint4','panda_joint5'
        ,'panda_joint6','panda_joint7','panda_finger_joint1','panda_finger_joint2']
        self.panda_rtb = rtb.models.URDF.Panda()
        

    def catlculate_trajectory(self):
        ## Location 1 : Behind the Object with Open Claws
        argv = sys.argv[1:]
        point = SE3(float(argv[0]),float(argv[1]),float(argv[2]))*SE3.Rx(180, unit='deg')
        joint_angles_ik_sol= (self.panda_rtb.ikine_LM(point))[0] ## joints angles for desired position 
        print("Transformation Matrix : \n",point)
        claw_state=[float(argv[3]),float(argv[4])]
        joint_angles_ik_sol=np.append(joint_angles_ik_sol,claw_state) ## adding open or close state
        
        # self.send_trajectory(joint_angles_ik_sol)
        
        ## Open the claws 

        

    def send_trajectory(self,joint_angles):
        print("\nAngles are \n",joint_angles)
        publihser_list.publish()
        
        ## trajecotry will be executed while the node will complete execution
        ## task will be sent before that with time delays


if __name__ == '__main__':
    panda_pick_and_place = Trajectoryfor_pick_and_place()
    panda_pick_and_place.catlculate_trajectory()

