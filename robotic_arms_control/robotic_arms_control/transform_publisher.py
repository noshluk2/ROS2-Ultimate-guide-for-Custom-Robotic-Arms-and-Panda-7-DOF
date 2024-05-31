#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped
from tf_transformations import quaternion_from_euler

class TransformPublisher(Node):
    def __init__(self):
        super().__init__('transforms_publisher')
        self._broadcaster = StaticTransformBroadcaster(self)
        self._timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'Base'
        t.child_frame_id = 'Link_0'
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 2.0

        q = quaternion_from_euler(0, 2.1, 0)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        # 2nd link
        t1 = TransformStamped()
        t1.header.stamp = self.get_clock().now().to_msg()
        t1.header.frame_id = 'Link_0'
        t1.child_frame_id = 'Link_1'
        t1.transform.translation.x = 2.0
        t1.transform.translation.y = 0.0
        t1.transform.translation.z = 0.0

        q = quaternion_from_euler(0, 0, 0)
        t1.transform.rotation.x = q[0]
        t1.transform.rotation.y = q[1]
        t1.transform.rotation.z = q[2]
        t1.transform.rotation.w = q[3]

        # Broadcast the transforms
        self._broadcaster.sendTransform(t)
        self._broadcaster.sendTransform(t1)

def main(args=None):
    rclpy.init(args=args)
    node = TransformPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
