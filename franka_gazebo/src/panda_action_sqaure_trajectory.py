#!/usr/bin/env python3
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import roboticstoolbox as rtb
from spatialmath import SE3
import numpy as np
def action_interface():

    rospy.init_node('dual_dual_arm_trajectorymsg_actionLib')
    panda_joints = ['panda_joint1','panda_joint2','panda_joint3','panda_joint4','panda_joint5'
        ,'panda_joint6','panda_joint7','panda_finger_joint1','panda_finger_joint2']
        
    waypoints_sqaure=[
                    [1.1 ,0.4 , 0.6],
                    [1.1 ,-0.4 ,0.6],
                    [0.7 ,-0.4 ,0.6],
                    [0.7 ,0.4 , 0.6],
                    [1.1 ,0.4 , 0.6],
                    ]
    waypoints_circle=[
                    [1.1 ,0.4 , 0.6],
                    [1.1 ,-0.4 ,0.6],
                    [0.7 ,-0.4 ,0.6],
                    [0.7 ,0.4 , 0.6],
                    
                    
                    ]
                
    joints_trajectory_points=[]
    panda_rtb = rtb.models.URDF.Panda()
    for i in range(5):
        point = SE3(waypoints_sqaure[i])
        joints_trajectory_points.append(np.append((panda_rtb.ikine_LM(point))[0] ,[0.4,0.4]  ))
    rospy.loginfo('Inverse kinematics solved lets start Action !')
            
    panda_client = actionlib.SimpleActionClient('panda/panda_controller/follow_joint_trajectory',
                                                    FollowJointTrajectoryAction)
    panda_client.wait_for_server()
    rospy.loginfo('Server connection = Success !')
    rospy.sleep(1)
    for i in range(5):
        trajectory_message = JointTrajectory()
        trajectory_message.joint_names = panda_joints
        trajectory_message.points.append(JointTrajectoryPoint())
        trajectory_message.points[0].positions = joints_trajectory_points[i]
        trajectory_message.points[0].velocities = [0.0 for i in panda_joints]
        trajectory_message.points[0].accelerations = [0.0 for i in panda_joints]
        trajectory_message.points[0].time_from_start = rospy.Duration(1)
        goal_positions = FollowJointTrajectoryGoal()
        goal_positions.trajectory = trajectory_message
        goal_positions.goal_time_tolerance = rospy.Duration(0)
        panda_client.send_goal(goal_positions)
        rospy.sleep(1)

   


if __name__ == '__main__':
    action_interface()
