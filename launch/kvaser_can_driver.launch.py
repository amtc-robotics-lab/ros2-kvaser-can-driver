from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('device_channel_num', default_value='1'),  # Number of device to be connected, no the channel id
        DeclareLaunchArgument('can_bitrate', default_value='500000'),  # 
        DeclareLaunchArgument('can_tx_config_path', default_value='can_tx_config.yaml'),  # 
        DeclareLaunchArgument('can_rx_config_path', default_value='can_rx_config.yaml'),  # 
        Node(
            package='ros_kvaser_can_driver',
            executable='kvaser_can_driver',
            name='kvaser_can_driver',
            output='screen',
            parameters=[
                {'device_channel_num': LaunchConfiguration('device_channel_num')},  # 
                {'can_bitrate': LaunchConfiguration('can_bitrate')},  # 
                {'can_tx_config_path': LaunchConfiguration('can_tx_config_path')},  # 
                {'can_rx_config_path': LaunchConfiguration('can_rx_config_path')},  # 
            ],
        )
    ])