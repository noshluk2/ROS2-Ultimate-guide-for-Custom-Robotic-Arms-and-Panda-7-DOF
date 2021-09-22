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
        rospy.init_node('Panda_traj_msgs_publisher')
        self.panda_traj_msg = JointTrajectory()
        self.contoller_name='/panda/arm_controller/command'
        self.trajectory_publihser = rospy.Publisher(self.contoller_name,JointTrajectory, queue_size=10)
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
        
        self.send_trajectory(joint_angles_ik_sol)
        
        ## Open the claws 

        

    def send_trajectory(self,joint_angles):
        print("\nAngles are \n",joint_angles)
        self.panda_traj_msg.joint_names = self.panda_joints
        self.panda_traj_msg.points.append(JointTrajectoryPoint())
        self.panda_traj_msg.points[0].positions = joint_angles
        self.panda_traj_msg.points[0].velocities = [0.0 for i in self.panda_joints]
        self.panda_traj_msg.points[0].accelerations = [0.0 for i in self.panda_joints]
        self.panda_traj_msg.points[0].time_from_start = rospy.Duration(3)
        self.trajectory_publihser.publish(self.panda_traj_msg)
        ## trajecotry will be executed while the node will complete execution
        ## task will be sent before that with time delays


if __name__ == '__main__':
    panda_pick_and_place = Trajectoryfor_pick_and_place()
    panda_pick_and_place.catlculate_trajectory()

