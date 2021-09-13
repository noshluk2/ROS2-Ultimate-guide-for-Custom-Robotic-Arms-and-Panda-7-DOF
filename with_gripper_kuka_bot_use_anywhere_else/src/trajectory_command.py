#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def perform_trajectory():
    rospy.init_node('KukaArm_traj_msgs_publisher')
    contoller_name='/manipulator/main_controller/command'
    trajectory_publihser = rospy.Publisher(contoller_name,JointTrajectory, queue_size=10)
                                
    dual_armRjoints = ['link_1_joint','link_2_joint','link_3_joint','link_4_joint','link_grip_l_joint','link_grip_r_joint']
    goal_positions = [1.57,0.84,0.53,-1.48,-0.01,0.02]
    rospy.sleep(1)
            ## creating a message to send Joint Trajectory type
    dual_armR_traj_msgs = JointTrajectory()
    dual_armR_traj_msgs.joint_names = dual_armRjoints
    dual_armR_traj_msgs.points.append(JointTrajectoryPoint())
    dual_armR_traj_msgs.points[0].positions = goal_positions
    dual_armR_traj_msgs.points[0].velocities = [0.0 for i in dual_armRjoints]
    dual_armR_traj_msgs.points[0].accelerations = [0.0 for i in dual_armRjoints]
    dual_armR_traj_msgs.points[0].time_from_start = rospy.Duration(3)
    rospy.sleep(1)
    trajectory_publihser.publish(dual_armR_traj_msgs)
            ## trajecotry will be executed while the node will complete execution
            ## task will be sent before that with time delays


if __name__ == '__main__':
    perform_trajectory()

