import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    package_path = get_package_share_directory(
        'intro_rover_description'
    )

    urdf_file = os.path.join(
        package_path,
        'urdf',
        'intro_rover_description.urdf'
    )

    gazebo_launch = os.path.join(
        get_package_share_directory('ros_gz_sim'),
        'launch',
        'gz_sim.launch.py'
    )

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[
                {
                    'robot_description': open(urdf_file).read()
                }
            ],
            output='screen'
        ),

        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock'
            ],
            output='screen'
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_launch),
            launch_arguments={
                'gz_args': '-r empty.sdf'
            }.items()
        ),

        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-name',
                'intro_rover',
                '-file',
                urdf_file
            ],
            output='screen'
        ),

        TimerAction(
            period=5.0,
            actions=[
                Node(
                    package='controller_manager',
                    executable='spawner',
                    arguments=[
                        'joint_state_broadcaster',
                        '--controller-manager',
                        '/controller_manager'
                    ],
                    output='screen'
                )
            ]
        ),

        TimerAction(
            period=10.0,
            actions=[
                Node(
                    package='controller_manager',
                    executable='spawner',
                    arguments=[
                        'wheel_controller',
                        '--controller-manager',
                        '/controller_manager'
                    ],
                    output='screen'
                )
            ]
        ),

        TimerAction(
            period=15.0,
            actions=[
                Node(
                    package='controller_manager',
                    executable='spawner',
                    arguments=[
                        'rover_controller',
                        '--controller-manager',
                        '/controller_manager'
                    ],
                    output='screen'
                )
            ]
        )
    ])
