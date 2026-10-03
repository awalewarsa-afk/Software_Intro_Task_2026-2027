import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState


class RoverDance(Node):

    def __init__(self):
        super().__init__('rover_dance')

        self.publisher = self.create_publisher(
            JointState,
            '/joint_states',
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
            'fr_wheel',
            'br_swerve_yaw',
            'br_wheel',
            'fl_swerve_yaw',
            'fl_wheel',
            'bl_swerve_yaw',
            'bl_wheel'
        ]

        self.step = 0

        self.timer = self.create_timer(
            1.0,
            self.dance
        )

    def dance(self):

        positions = [0.0] * 14

        if self.step == 0:
            positions[0] = 0.5
            positions[1] = 0.5

        elif self.step == 1:
            positions[0] = -0.5
            positions[1] = -0.5

        elif self.step == 2:
            positions[2] = 0.5
            positions[3] = 0.5

        elif self.step == 3:
            positions[2] = -0.5
            positions[3] = -0.5

        elif self.step == 4:
            positions[4] = 0.5
            positions[5] = 0.5

        elif self.step == 5:
            positions[4] = -0.5
            positions[5] = -0.5

        elif self.step == 6:
            positions[6] = 0.5
            positions[8] = -0.5
            positions[10] = 0.5
            positions[12] = -0.5

        elif self.step == 7:
            positions[6] = -0.5
            positions[8] = 0.5
            positions[10] = -0.5
            positions[12] = 0.5

        msg = JointState()

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = self.joints
        msg.position = positions

        self.publisher.publish(msg)

        self.step = (self.step + 1) % 8


def main(args=None):

    rclpy.init(args=args)

    node = RoverDance()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
