from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'robotic_arms_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luqman',
    maintainer_email='noshluk2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'transforms_pub = robotic_arms_control.transform_publisher:main',
            'jtc_controller_test = robotic_arms_control.joint_controller_test:main',
            'kinematic_solver = robotic_arms_control.kinematic_solver:main',
            'jtc_multi_goals = robotic_arms_control.jtc_multi_goals:main',

        ],
    },
)
