import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray


class ManualJointController(Node):

    def __init__(self):
        super().__init__('manual_joint_controller')

        self.publisher = self.create_publisher(
            Float64MultiArray,
            '/rover_controller/commands',
            10
        )

        self.joints = [
            'shoulder_yaw',
            'shoulder_pitch',
            'elbow_pitch',
            'elbow_roll',
            'wrist_pitch',
            'wrist_roll',
            'fr_swerve_yaw',
            'br_swerve_yaw',
            'fl_swerve_yaw',
            'bl_swerve_yaw'
        ]

        self.timer = self.create_timer(0.1, self.publish_command)

        self.joint_positions = [0.0] * len(self.joints)

    def publish_command(self):

        msg = Float64MultiArray()

        msg.data = self.joint_positions

        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = ManualJointController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
