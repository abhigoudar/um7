import launch_ros.actions
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, GroupAction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition, LaunchConfigurationEquals, LaunchConfigurationNotEquals

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name="port_id",
            default_value="/dev/um7_imu",
        ),
        #
        #
        #
        launch_ros.actions.Node(
            name="um7_driver",
            executable="um7_driver",
            package="umx_driver",
            output="screen",
            emulate_tty=True,
            parameters=[{
                "port" : LaunchConfiguration("port_id")
            }]
        )
    ])
