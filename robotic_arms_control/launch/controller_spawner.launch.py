from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkgPath = get_package_share_directory('robotic_arms_control')
    gazeboLaunchFile = os.path.join(pkgPath, 'launch', 'gazebo_bringup.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazeboLaunchFile)
        ),

        Node(
            package='controller_manager',
            executable='spawner',
            output='screen',
            arguments=["joint_state_broadcaster"]),

        Node(
            package='controller_manager',
            executable='spawner',
            output='screen',
            arguments=["joint_trajectory_controller"]),
    ])