#!/usr/bin/env python3

import rclpy as rlc
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('my_turtle_controller')
        self.get_logger().info('ROS2 a')
        self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('ROS2 b')

def main(args=None):
    rlc.init(args=args)
    node = MyNode()
    rlc.spin(node)
    rlc.shutdown()

if __name__ == '__main__':
    main()