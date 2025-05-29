import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_nav2_bringup = get_package_share_directory('nav2_bringup')

    map_dir = LaunchConfiguration('map')
    param_dir = LaunchConfiguration('params_file')
    use_sim_time = LaunchConfiguration('use_sim_time')

    declare_map_cmd = DeclareLaunchArgument(
        'map',
        default_value='/root/rmf_s502_real/map.yaml',
        description='マップファイルへのフルパス')

    declare_params_cmd = DeclareLaunchArgument(
        'params_file',
        default_value='/root/rmf_s502_real/limo_param.yaml',
        description='パラメータファイルへのフルパス')

    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Sim timeを使うか')

    nav_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav2_bringup, 'launch', 'bringup_launch.py')),
        launch_arguments={
            'map': map_dir,
            'params_file': param_dir,
            'use_sim_time': use_sim_time
        }.items()
    )

    return LaunchDescription([
        declare_map_cmd,
        declare_params_cmd,
        declare_use_sim_time_cmd,
        nav_launch
    ])
