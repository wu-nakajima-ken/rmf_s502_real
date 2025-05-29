import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 定数としてパスを設定
    pkg_nav2_bringup = get_package_share_directory('nav2_bringup')
    
    map_dir = LaunchConfiguration('map', default='/root/rmf_s502_real/map.yaml')
    param_dir = LaunchConfiguration('params_file', default='/root/rmf_s502_real/limo_param.yaml')
    
    # ランチ引数を定義
    declare_map_cmd = DeclareLaunchArgument(
        'map',
        default_value='/root/rmf_s502_real/map.yaml',
        description='マップファイルへのフルパス')
    
    declare_params_cmd = DeclareLaunchArgument(
        'params_file',
        default_value='/root/rmf_s502_real/limo_param.yaml',
        description='パラメータファイルへのフルパス')
    
    # Nav2を起動する
    nav_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_nav2_bringup, 'launch', 'bringup_launch.py')),
        launch_arguments={
            'map': map_dir,
            'params_file': param_dir,
            'use_sim_time': 'true',
        }.items()
    )
    #バッテリー
    # bat_status_launch = Node(
    #         package="limo_battery_pub",
    #         executable="limo_battery_pub",
    #         output="screen"
    #     )

        
    return LaunchDescription([
        declare_map_cmd,
        declare_params_cmd,
        # bat_status_launch,
        nav_launch
    ])

