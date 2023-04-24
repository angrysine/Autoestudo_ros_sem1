#!/usr/bin/env python3

import rclpy as rlc
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('my_turtle_controller')
        self.get_logger().info('Hello ROS2')

def main(args=None):
    rlc.init(args=args)
    node = MyNode()
    rlc.spin(node)
    rlc.shutdown()

if __name__ == '__main__':
    main()