#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import time

class TrajectoryTest(Node):

    def __init__(self):
        super().__init__('trajectory_test')
        topic_name = "/joint_trajectory_controller/joint_trajectory"
        self.trajectory_publisher = self.create_publisher(JointTrajectory, topic_name, 10)
        self.joints = ['panda_joint1','panda_joint2','panda_joint3',
                       'panda_joint4','panda_joint5','panda_joint6',
                       'panda_joint7','panda_finger_joint1']
        self.goal_positions_list = [
                            [1.911, 0.8322, -0.4118, -1.557, -2.733, 0.8391, -0.5577, 0.032],
                            [-1.6132166399999996, 1.3816826400000002, 0.32913327999999975, 0.1670647999999999, 0.5794600000000001, 1.2865429999999998, 0.0, 0.0],
                            [-1.6132166399999996, -0.14278679999999988, -0.4230057999999999, -1.2219676, -0.4230057999999999, 1.938753, 1.1119837399999999, 0.03892],
                            [-1.6132166399999996, -0.39063647999999995, 2.8973, -0.9298729999999997, -0.04693625999999984, 1.59229, 1.1119837399999999, 0.03892],
                            [1.6132166399999996, 1.62953232, 0.32913327999999975, 0.1670647999999999, 0.4230057999999999, 1.938753, 1.1119837399999999, 0.03892],
                            [-1.6132166399999996, -1.4768738399999999, 2.8973, -0.3294730000000001, 0.26597214000000013, 1.857321, 0.82978672, 0.03892]
                        ]
        self.current_goal_index = 0
        self.trajectory_active = False
        self.timer = self.create_timer(3, self.timer_callback)
        self.get_logger().info('Controller is running and publishing to topic: {}'.format(topic_name))

    def timer_callback(self):
        if not self.trajectory_active and self.current_goal_index < len(self.goal_positions_list):
            self.publish_trajectory(self.goal_positions_list[self.current_goal_index])
            self.current_goal_index += 1
            self.trajectory_active = True

    def publish_trajectory(self, goal_positions):
        trajectory_msg = JointTrajectory()
        trajectory_msg.joint_names = self.joints
        point = JointTrajectoryPoint()
        point.positions = goal_positions
        point.time_from_start = Duration(sec=2)
        trajectory_msg.points.append(point)
        self.trajectory_publisher.publish(trajectory_msg)
        self.get_logger().info('Published trajectory: {}'.format(goal_positions))
        self.create_timer(3, self.trajectory_complete_callback)  # Wait for the trajectory to complete

    def trajectory_complete_callback(self):
        self.get_logger().info('Completed trajectory {}'.format(self.current_goal_index))
        time.sleep(2)
        self.trajectory_active = False

def main(args=None):
    rclpy.init(args=args)
    trajectory_publisher_node = TrajectoryTest()
    rclpy.spin(trajectory_publisher_node)
    trajectory_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
