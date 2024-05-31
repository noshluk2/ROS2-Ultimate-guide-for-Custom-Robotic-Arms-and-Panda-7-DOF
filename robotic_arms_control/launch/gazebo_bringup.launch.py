from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory , get_package_prefix
import os
from launch.actions import ExecuteProcess

def generate_launch_description():
    pkgPath = get_package_share_directory('robotic_arms_control')
    urdfFile = os.path.join(pkgPath, 'urdf', 'panda_arm.urdf')

    mesh_pkg_share_dir = os.pathsep + os.path.join(get_package_prefix('franka_description'), 'share')

    if 'GAZEBO_MODEL_PATH' in os.environ:
        os.environ['GAZEBO_MODEL_PATH'] += mesh_pkg_share_dir
    else:
        os.environ['GAZEBO_MODEL_PATH'] =  mesh_pkg_share_dir

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            arguments=[urdfFile]),

        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='robot_spawner',
            output='screen',
            arguments=["-topic", "/robot_description", "-entity", "bazu"]),

    ])